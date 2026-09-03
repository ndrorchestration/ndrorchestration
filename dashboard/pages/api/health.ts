import type { NextApiRequest, NextApiResponse } from 'next';
import { ORBIT_VERSION } from '../../data/config';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.setHeader('Cache-Control', 'no-store, max-age=0');
  res.setHeader('X-ORBIT-Version', ORBIT_VERSION);
  if (req.method !== 'GET') {
    res.setHeader('Allow', 'GET');
    return res.status(405).json({ status: 'METHOD_NOT_ALLOWED' });
  }
  return res.status(200).json({ status: 'ok', service: 'orbit', version: ORBIT_VERSION, timestamp: new Date().toISOString() });
}
