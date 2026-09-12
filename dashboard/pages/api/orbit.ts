import type { NextApiRequest, NextApiResponse } from 'next';
import { orbitSnapshot, GateState } from '../../data/orbit';
import { orbitConfig, EVIDENCE_SCHEMA } from '../../data/config';

const GITHUB_API = 'https://api.github.com';

function readinessStateFor(gates: typeof orbitSnapshot.gates) {
  if (gates.some(gate => gate.state === 'blocked')) return 'BLOCKED';
  if (gates.some(gate => gate.state === 'warning' || gate.state === 'not-established')) return 'ATTENTION';
  return 'CLEAR';
}

async function github(path: string) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), orbitConfig.githubTimeoutMs);
  try {
    const headers: Record<string, string> = {
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'User-Agent': 'ORBIT-evidence-observer',
    };
    if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
    const response = await fetch(`${GITHUB_API}${path}`, { headers, signal: controller.signal });
    if (!response.ok) throw new Error(`GitHub ${response.status}`);
    return response.json();
  } finally {
    clearTimeout(timeout);
  }
}

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  res.setHeader('Cache-Control', 'no-store, max-age=0');
  res.setHeader('X-ORBIT-Evidence-Schema', EVIDENCE_SCHEMA);
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const [branch, readme] = await Promise.all([
      github(`/repos/${orbitConfig.repository}/branches/${encodeURIComponent(orbitConfig.branch)}`),
      github(`/repos/${orbitConfig.repository}/contents/README.md?ref=${encodeURIComponent(orbitConfig.branch)}`),
    ]);

    if (!branch?.commit?.sha || !readme?.content || typeof readme.content !== 'string') {
      throw new Error('GitHub response missing required evidence fields');
    }

    const currentHead = branch.commit.sha;
    if (!/^[0-9a-f]{40}$/.test(currentHead)) throw new Error('GitHub returned an invalid commit SHA');

    const readmeText = Buffer.from(readme.content, 'base64').toString('utf8');
    const declaredN0 = /empirical\s+N\s*=\s*0/i.test(readmeText);
    const declaredUnauthorized = /(?:NOT\s+AUTHORIZED|authorization[^\n]{0,80}NOT\s+(?:GRANTED|AUTHORIZED))/i.test(readmeText);
    const declaredFailClosed = /FAIL-CLOSED/i.test(readmeText);
    const deploymentCommit = process.env.VERCEL_GIT_COMMIT_SHA || null;
    const sourceFreshness = currentHead === orbitSnapshot.head ? 'ALIGNED' : 'DRIFT';
    const deploymentFreshness = deploymentCommit ? (deploymentCommit === currentHead ? 'ALIGNED' : 'DRIFT') : 'UNAVAILABLE';
    const gates = orbitSnapshot.gates.map(g => ({ ...g }));

    if (!declaredN0 || !declaredUnauthorized || !declaredFailClosed) {
      const freeze = gates.find(g => g.id === 'FREEZE');
      if (freeze) {
        freeze.state = 'blocked';
        freeze.evidence = 'DGAF authority check incomplete';
        freeze.detail = 'Canonical DGAF documentation does not simultaneously affirm FAIL-CLOSED, NOT AUTHORIZED, and empirical N = 0.';
      }
    }

    if (sourceFreshness === 'DRIFT') {
      const doc = gates.find(g => g.id === 'DOC');
      if (doc) {
        doc.state = 'warning';
        doc.evidence = `DGAF HEAD drift: ${currentHead.slice(0, 8)}`;
        doc.detail = 'The bundled ORBIT snapshot does not match current DGAF main; live evidence is newer than the snapshot.';
      }
    }

    const fetchedAt = new Date().toISOString();
    return res.status(200).json({
      generatedAt: fetchedAt,
      overallState: readinessStateFor(gates),
      authority: {
        role: 'observer-only',
        repository: orbitConfig.repository,
        branch: orbitConfig.branch,
        note: 'ORBIT reports evidence state; it does not grant freeze, authorization, or empirical authority.',
      },
      snapshot: { ...orbitSnapshot, head: currentHead, gates },
      live: {
        fetchedAt,
        sourceFreshness,
        github: {
          repository: orbitConfig.repository,
          branch: orbitConfig.branch,
          currentHead,
          signatureVerified: Boolean(branch.commit?.commit?.verification?.verified),
          readmeSha: readme.sha,
          readmeState: {
            failClosed: declaredFailClosed,
            empiricalN0: declaredN0,
            unauthorized: declaredUnauthorized,
          },
        },
        vercel: {
          commit: deploymentCommit,
          freshness: deploymentFreshness,
          url: process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : null,
        },
      },
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown error';
    return res.status(503).json({
      generatedAt: new Date().toISOString(),
      overallState: 'UNAVAILABLE',
      authority: {
        role: 'observer-only',
        repository: orbitConfig.repository,
        branch: orbitConfig.branch,
      },
      snapshot: orbitSnapshot,
      live: { status: 'UNAVAILABLE', error: message },
    });
  }
}
