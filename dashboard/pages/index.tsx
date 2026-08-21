import type { NextPage } from 'next';
import Head from 'next/head';
import { useEffect, useState } from 'react';
import { orbitSnapshot as initialSnapshot, readinessScore, GateState } from '../data/orbit';

const stateLabel: Record<GateState, string> = { verified: 'VERIFIED', ready: 'READY', blocked: 'BLOCKED', 'not-established': 'NOT ESTABLISHED', warning: 'WARNING' };
const stateClass: Record<GateState, string> = { verified: 'ok', ready: 'ready', blocked: 'bad', 'not-established': 'muted', warning: 'warn' };

type Snapshot = typeof initialSnapshot;

const Home: NextPage = () => {
  const [snapshot, setSnapshot] = useState<Snapshot>(initialSnapshot);
  const [live, setLive] = useState<{ sourceFreshness?: string; currentHead?: string; fetchedAt?: string } | null>(null);
  const [refreshing, setRefreshing] = useState(false);

  async function refresh() {
    setRefreshing(true);
    try {
      const response = await fetch('/api/orbit');
      const payload = await response.json();
      if (payload.snapshot) setSnapshot(payload.snapshot);
      setLive({ sourceFreshness: payload.live?.sourceFreshness, currentHead: payload.live?.github?.currentHead, fetchedAt: payload.live?.fetchedAt });
    } finally { setRefreshing(false); }
  }

  useEffect(() => { refresh(); }, []);
  const score = readinessScore();
  const verified = snapshot.gates.filter(g => g.state === 'verified').length;
  const blockers = snapshot.gates.filter(g => g.state === 'blocked').length;

  return <>
    <Head><title>ORBIT — Evidence & Readiness Command Center</title><meta name="description" content="Evidence-first readiness control plane for DGAF/PDMAL." /></Head>
    <main className="shell">
      <header className="topbar"><div><span className="eyebrow">ORBIT / NDR ORCHESTRATION</span><h1>Evidence & Readiness Command Center</h1><p>One operational surface for what is true, what proves it, and what remains blocked.</p></div><div className="score"><strong>{score}%</strong><span>READINESS INDEX</span><button onClick={refresh} disabled={refreshing}>{refreshing ? 'REFRESHING' : 'REFRESH EVIDENCE'}</button></div></header>
      <section className="state panel"><div><span className="label">CURRENT EPISTEMIC STATE</span><h2>{snapshot.epistemicState}</h2></div><div className="stop">EMPIRICAL EXECUTION STOPPED</div></section>
      <section className="metrics"><div className="metric"><span>HEAD</span><b>{snapshot.head}</b><small>dashboard evidence snapshot</small></div><div className="metric"><span>LIVE SOURCE</span><b>{live?.currentHead?.slice(0, 8) || '—'}</b><small>{live?.sourceFreshness || 'checking GitHub'}</small></div><div className="metric"><span>EMPIRICAL N</span><b>{snapshot.empiricalN}</b><small>efficacy not established</small></div><div className="metric"><span>BLOCKERS</span><b>{blockers}</b><small>authorization / execution gates</small></div></section>
      <div className="grid">
        <section className="panel"><div className="sectionHead"><div><span className="label">EVIDENCE GATES</span><h2>Governance matrix</h2></div><span className="tiny">{verified}/{snapshot.gates.length} verified</span></div><div className="gates">{snapshot.gates.map(g => <article className="gate" key={g.id}><div className={`dot ${stateClass[g.state]}`} /><div className="gateMain"><div><b>{g.id} · {g.name}</b><span className={`badge ${stateClass[g.state]}`}>{stateLabel[g.state]}</span></div><p>{g.detail}</p><small>{g.evidence}</small></div></article>)}</div></section>
        <section className="panel"><div className="sectionHead"><div><span className="label">CLAIM INTEGRITY</span><h2>Propagation monitor</h2></div><span className="tiny">fail-closed</span></div>{snapshot.claims.map(c => <article className="claim" key={c.claim}><div className="claimTitle"><b>{c.claim}</b><span className={`badge ${c.status === 'warning' ? 'warn' : 'bad'}`}>{c.status.toUpperCase()}</span></div><div className="bar"><i style={{ width: `${c.occurrences ? (c.qualified / c.occurrences) * 100 : 0}%` }} /></div><p>{c.occurrences} occurrences · {c.qualified} qualified · {c.bare} bare</p></article>)}<div className="rule">Claims do not upgrade epistemic status. Evidence does.</div></section>
      </div>
      <section className="panel deployment"><div><span className="label">TRACE</span><h2>Immutable evidence boundary</h2><p>Historical evidence: <code>{snapshot.historicalEvidence}</code> · Deployment: <code>{snapshot.deployment}</code></p><p>Last live reconciliation: <code>{live?.fetchedAt || 'pending'}</code></p></div><a href="/api/orbit">JSON endpoint →</a></section>
      <footer>ORBIT v0.1 · live GitHub reconciliation · snapshot-backed · DGAF/PDMAL pilot remains unauthorized</footer>
    </main>
    <style jsx global>{`*{box-sizing:border-box}body{margin:0;background:#07090d;color:#e7eaf0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,sans-serif}.shell{max-width:1240px;margin:auto;padding:42px 28px 60px}.topbar{display:flex;justify-content:space-between;gap:30px;align-items:flex-start;border-bottom:1px solid #202630;padding-bottom:30px}.eyebrow,.label{font-size:11px;letter-spacing:.13em;color:#778091;font-weight:700}.topbar h1{font-size:30px;margin:8px 0}.topbar p,.panel p,.metric small{color:#8992a2}.score{text-align:right}.score strong{display:block;font-size:40px}.score span,.tiny{font-size:10px;color:#6f7887;letter-spacing:.1em}.score button{margin-top:10px;background:#151b24;border:1px solid #303947;color:#aeb8c7;border-radius:6px;padding:7px 10px;font-size:10px}.panel{background:#0d1118;border:1px solid #202630;border-radius:12px;padding:22px}.state{margin:22px 0;display:flex;justify-content:space-between;align-items:center;gap:20px}.state h2{font-size:17px;font-weight:500;margin:9px 0 0}.stop{border:1px solid #6f3333;color:#ff8d8d;padding:9px 12px;border-radius:7px;font-size:10px;font-weight:800;letter-spacing:.08em;white-space:nowrap}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:22px}.metric{background:#0d1118;border:1px solid #202630;border-radius:10px;padding:17px}.metric span{display:block;font-size:10px;color:#697382;font-weight:700;letter-spacing:.1em}.metric b{display:block;margin:9px 0 4px;font-size:18px;font-family:ui-monospace,monospace}.metric small{font-size:11px}.grid{display:grid;grid-template-columns:1.45fr 1fr;gap:22px}.sectionHead{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:1px solid #202630;padding-bottom:15px;margin-bottom:6px}.sectionHead h2,.deployment h2{font-size:18px;margin:7px 0 0}.gate{display:flex;gap:13px;padding:16px 4px;border-bottom:1px solid #1b2028}.dot{width:8px;height:8px;border-radius:50%;margin-top:7px;flex:none}.dot.ok{background:#54d69a}.dot.ready{background:#6ba8ff}.dot.bad{background:#ff6e72}.dot.warn{background:#e5b75c}.dot.muted{background:#657080}.gateMain{width:100%}.gateMain>div,.claimTitle{display:flex;justify-content:space-between;gap:10px;align-items:center}.gateMain p{font-size:12px;margin:7px 0}.gateMain small{font-size:10px;color:#667080}.badge{font-size:9px;border:1px solid;padding:3px 6px;border-radius:4px;font-weight:800;letter-spacing:.06em}.badge.ok{color:#65dca3;border-color:#275d45}.badge.ready{color:#76aeff;border-color:#294a77}.badge.bad{color:#ff8085;border-color:#71363a}.badge.warn{color:#e8bf68;border-color:#665225}.badge.muted{color:#8490a0;border-color:#39414d}.claim{padding:18px 0;border-bottom:1px solid #1b2028}.claimTitle{font-size:12px}.bar{height:5px;background:#202630;border-radius:10px;margin:15px 0 8px;overflow:hidden}.bar i{display:block;height:100%;background:#d2a94d}.claim p{font-size:11px;margin:0}.rule{margin-top:18px;padding:12px;background:#111720;border-left:2px solid #657080;font-size:11px;color:#aab2bf}.deployment{margin-top:22px;display:flex;justify-content:space-between;align-items:center}.deployment p{font-size:12px}.deployment a{color:#91b8ff;text-decoration:none;font-size:12px}.deployment code{font-family:ui-monospace,monospace;color:#c8d0dd}footer{text-align:center;color:#4d5663;font-size:10px;margin-top:30px}@media(max-width:800px){.topbar,.state,.deployment{flex-direction:column}.metrics,.grid{grid-template-columns:1fr}.score{text-align:left}}`}</style>
  </>;
};
export default Home;
