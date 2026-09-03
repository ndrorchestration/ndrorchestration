import type { NextApiRequest, NextApiResponse } from 'next';
import { EVIDENCE_SCHEMA, ORBIT_VERSION } from '../../data/config';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.setHeader('Cache-Control', 'public, max-age=3600, immutable');
  res.setHeader('X-ORBIT-Version', ORBIT_VERSION);
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ error: 'Method Not Allowed' });
  }
  return res.status(200).json({
    service: 'orbit', version: ORBIT_VERSION, evidenceSchema: EVIDENCE_SCHEMA,
    guarantees: ['source-head semantics', 'fail-closed governance', 'snapshot-backed evidence', 'claims do not upgrade epistemic status'],
  });
}
