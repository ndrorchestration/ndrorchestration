import type { NextApiRequest, NextApiResponse } from 'next';
import { orbitSnapshot, GateState } from '../../data/orbit';

const GITHUB_API = 'https://api.github.com';
const REPO = 'ndrorchestration/ndrorchestration';
const GITHUB_TIMEOUT_MS = 5000;

function readinessScoreFor(gates: typeof orbitSnapshot.gates) {
  const weights: Record<GateState, number> = { verified: 1, ready: 0.75, warning: 0.5, 'not-established': 0.25, blocked: 0 };
  const total = gates.reduce((sum, gate) => sum + weights[gate.state], 0);
  return Math.round((total / gates.length) * 100);
}

async function github(path: string) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), GITHUB_TIMEOUT_MS);
  try {
    const headers: Record<string, string> = {
      Accept: 'application/vnd.github+json',
      'X-GitHub-Api-Version': '2022-11-28',
      'User-Agent': 'ORBIT-evidence-command-center',
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
  res.setHeader('X-ORBIT-Evidence-Schema', 'orbit.evidence.v2');
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const [branch, readme] = await Promise.all([
      github(`/repos/${REPO}/branches/main`),
      github(`/repos/${REPO}/contents/README.md?ref=main`),
    ]);
    if (!branch?.commit?.sha || !readme?.content || typeof readme.content !== 'string') {
      throw new Error('GitHub response missing required evidence fields');
    }
    const currentHead = branch.commit.sha;
    if (!/^[0-9a-f]{40}$/.test(currentHead)) throw new Error('GitHub returned an invalid commit SHA');

    const readmeText = Buffer.from(readme.content, 'base64').toString('utf8');
    const declaredN0 = /Current empirical state:\*\*\s*N\s*=\s*0/i.test(readmeText);
    const declaredUnauthorized = /Pilot authorization:\*\*\s*Not granted/i.test(readmeText);
    const deploymentCommit = process.env.VERCEL_GIT_COMMIT_SHA || null;
    const sourceFreshness = currentHead === orbitSnapshot.head ? 'ALIGNED' : 'DRIFT';
    const deploymentFreshness = deploymentCommit ? (deploymentCommit === currentHead ? 'ALIGNED' : 'DRIFT') : 'UNAVAILABLE';
    const gates = orbitSnapshot.gates.map(g => ({ ...g }));

    if (!declaredN0 || !declaredUnauthorized) {
      const freeze = gates.find(g => g.id === 'FREEZE');
      if (freeze) {
        freeze.state = 'blocked';
        freeze.evidence = 'README contradiction';
        freeze.detail = 'Repository documentation does not affirm the required fail-closed experimental state.';
      }
    }
    if (sourceFreshness === 'DRIFT') {
      const doc = gates.find(g => g.id === 'DOC');
      if (doc) {
        doc.state = 'warning';
        doc.evidence = `HEAD drift: ${currentHead.slice(0, 8)}`;
        doc.detail = 'Dashboard snapshot does not match current main HEAD; refresh evidence before treating the snapshot as current.';
      }
    }

    return res.status(200).json({
      generatedAt: new Date().toISOString(),
      readiness: readinessScoreFor(gates),
      snapshot: { ...orbitSnapshot, gates },
      live: {
        fetchedAt: new Date().toISOString(),
        sourceFreshness,
        github: {
          branch: 'main', currentHead,
          signatureVerified: Boolean(branch.commit?.commit?.verification?.verified),
          readmeSha: readme.sha,
          readmeState: { empiricalN0: declaredN0, pilotUnauthorized: declaredUnauthorized },
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
      readiness: readinessScoreFor(orbitSnapshot.gates),
      snapshot: orbitSnapshot,
      live: { status: 'UNAVAILABLE', error: message },
    });
  }
}
