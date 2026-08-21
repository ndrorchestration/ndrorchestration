import type { NextApiRequest, NextApiResponse } from 'next';
import { orbitSnapshot, readinessScore } from '../../data/orbit';

const GITHUB_API = 'https://api.github.com';
const REPO = 'ndrorchestration/ndrorchestration';

async function github(path: string) {
  const headers: Record<string, string> = {
    Accept: 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28',
    'User-Agent': 'ORBIT-evidence-command-center',
  };
  if (process.env.GITHUB_TOKEN) headers.Authorization = `Bearer ${process.env.GITHUB_TOKEN}`;
  const response = await fetch(`${GITHUB_API}${path}`, { headers });
  if (!response.ok) throw new Error(`GitHub ${response.status}`);
  return response.json();
}

export default async function handler(_req: NextApiRequest, res: NextApiResponse) {
  const fetchedAt = new Date().toISOString();
  try {
    const branch = await github(`/repos/${REPO}/branches/main`);
    const readme = await github(`/repos/${REPO}/contents/README.md?ref=main`);
    const readmeText = Buffer.from(readme.content, 'base64').toString('utf8');
    const currentHead = branch.commit.sha;
    const declaredN0 = /Current empirical state:\*\*\s*N\s*=\s*0/i.test(readmeText);
    const declaredUnauthorized = /Pilot authorization:\*\*\s*Not granted/i.test(readmeText);

    // Vercel and CI may provide the exact source commit. Never infer source
    // identity from a PR's synthetic merge SHA.
    const deploymentCommit = process.env.VERCEL_GIT_COMMIT_SHA || null;
    const observedSourceCommit = process.env.ORBIT_SOURCE_SHA || deploymentCommit || null;
    const snapshotIsCurrent = observedSourceCommit ? observedSourceCommit === currentHead : false;
    const sourceFreshness = snapshotIsCurrent ? 'ALIGNED' : observedSourceCommit ? 'DRIFT' : 'UNAVAILABLE';
    const deploymentFreshness = deploymentCommit ? (deploymentCommit === currentHead ? 'ALIGNED' : 'DRIFT') : 'UNAVAILABLE';

    const gates = orbitSnapshot.gates.map(g => ({ ...g }));
    if (!snapshotIsCurrent) {
      const doc = gates.find(g => g.id === 'DOC');
      if (doc) {
        doc.state = 'warning';
        doc.evidence = observedSourceCommit ? `Observed source drift: ${observedSourceCommit.slice(0, 8)}` : 'No source snapshot identity';
        doc.detail = 'Live repository state was fetched successfully, but the stored evidence snapshot is not proven current.';
      }
    }

    res.status(200).json({
      generatedAt: fetchedAt,
      readiness: readinessScore(),
      snapshot: { ...orbitSnapshot, gates },
      live: {
        status: 'LIVE',
        fetchedAt,
        sourceFreshness,
        github: {
          branch: 'main',
          currentHead,
          observedSourceCommit,
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
    res.status(200).json({
      generatedAt: fetchedAt,
      readiness: readinessScore(),
      snapshot: orbitSnapshot,
      live: { status: 'UNAVAILABLE', error: error instanceof Error ? error.message : 'unknown error' },
    });
  }
}
