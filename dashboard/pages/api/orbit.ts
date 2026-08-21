import type { NextApiRequest, NextApiResponse } from 'next';
import { orbitSnapshot, readinessScore } from '../../data/orbit';

export default function handler(_req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ generatedAt: new Date().toISOString(), readiness: readinessScore(), snapshot: orbitSnapshot });
}
