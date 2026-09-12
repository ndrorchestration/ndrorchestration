import type { NextPage } from 'next';
import Head from 'next/head';

const systems = [
  {
    name: 'DGAF',
    type: 'Governance / multi-agent systems',
    description: 'Dynamic Governance Agentic Formation separates capability, evidence, verification, authority, and permission to act in governed agentic systems.',
    boundary: 'PRE-FREEZE · FAIL-CLOSED · NOT AUTHORIZED · empirical N = 0',
    href: 'https://github.com/ndrorchestration/DGAF-Framework',
  },
  {
    name: 'Intellectro',
    type: 'Independent application',
    description: 'A separate governed application program with its own runtime, data, and product boundaries.',
    boundary: 'Independent project; DGAF patterns may inform it without transferring DGAF authority or evidence.',
    href: 'https://intellectro.vercel.app/',
  },
  {
    name: 'Driftwatch',
    type: 'Evaluation / drift instrumentation',
    description: 'Failure-aware evaluation and drift instrumentation with reproducible synthetic benchmark apparatus.',
    boundary: 'Synthetic benchmark evidence does not establish real-world calibration or efficacy.',
    href: 'https://driftwatch-gamma.vercel.app/',
  },
  {
    name: 'AOGA Dashboard',
    type: 'Operational surface',
    description: 'A bounded operational dashboard for the AOGA project and its currently implemented runtime/data surfaces.',
    boundary: 'Deployment state is not treated as proof of end-to-end efficacy or broader governance authority.',
    href: 'https://aoga-dashboard.vercel.app/',
  },
];

const Home: NextPage = () => (
  <>
    <Head>
      <title>NDR AI Systems — Andrew Hensel</title>
      <meta name="description" content="AI systems design, orchestration, evaluation, governance, provenance, and reproducible experimentation by Andrew Hensel." />
    </Head>
    <main className="shell">
      <header className="hero">
        <span className="eyebrow">NDR AI SYSTEMS</span>
        <h1>Andrew “Ndr / Ender” Hensel</h1>
        <h2>AI Systems Designer · Orchestration · Evaluation · Governance</h2>
        <p>I design and evaluate AI systems with an emphasis on multi-agent orchestration, prompt and evaluation methodology, provenance, governance, reproducible experimentation, and trustworthy deployment controls.</p>
        <div className="actions">
          <a className="primary" href="https://github.com/ndrorchestration">GitHub</a>
          <a href="/orbit">Open ORBIT evidence observer</a>
        </div>
      </header>

      <section className="principle">
        <span>WORKING PRINCIPLE</span>
        <strong>Build the apparatus before claiming the result.</strong>
        <p>Implementation, testing, verification, deployment, authorization, and empirical efficacy are kept as distinct evidence states.</p>
      </section>

      <section>
        <div className="sectionHead">
          <div><span className="eyebrow">FEATURED SYSTEMS</span><h2>Current deployed and research surfaces</h2></div>
          <p>Each project carries an explicit evidence boundary rather than inheriting claims from the rest of the ecosystem.</p>
        </div>
        <div className="cards">
          {systems.map(system => (
            <article className="card" key={system.name}>
              <span className="type">{system.type}</span>
              <h3>{system.name}</h3>
              <p>{system.description}</p>
              <div className="boundary"><b>Evidence boundary</b><span>{system.boundary}</span></div>
              <a href={system.href}>View system →</a>
            </article>
          ))}
        </div>
      </section>

      <section className="architecture">
        <div><span className="eyebrow">PORTFOLIO ARCHITECTURE</span><h2>Research and engineering focus</h2></div>
        <div className="lanes">
          <div><b>Governance</b><span>DGAF · evidence gates · provenance · authorization boundaries</span></div>
          <div><b>Orchestration</b><span>multi-agent formations · topology/choreography · control-plane design</span></div>
          <div><b>Evaluation</b><span>Driftwatch · benchmark methodology · prompt/evaluator systems</span></div>
          <div><b>Experimental interfaces</b><span>spatial, acoustic, topology, and geometric research tools</span></div>
        </div>
      </section>

      <section className="observer">
        <div>
          <span className="eyebrow">EVIDENCE OBSERVABILITY</span>
          <h2>ORBIT is deliberately subordinate.</h2>
          <p>ORBIT is a read-only observer that reconciles evidence and surfaces blockers. It does not become a source of governance authority simply because it can display or reconcile state.</p>
        </div>
        <a href="/orbit">View ORBIT →</a>
      </section>

      <footer>Public portfolio surface · project-specific repositories and evidence records remain authoritative for their own state.</footer>
    </main>
    <style jsx global>{`*{box-sizing:border-box}body{margin:0;background:#07090d;color:#edf0f5;font-family:Inter,ui-sans-serif,system-ui,-apple-system,sans-serif}.shell{max-width:1180px;margin:auto;padding:58px 28px 46px}.eyebrow,.type{font-size:11px;letter-spacing:.14em;font-weight:800;color:#7e8999}.hero{padding:32px 0 48px;border-bottom:1px solid #202630}.hero h1{font-size:48px;line-height:1.05;margin:12px 0 8px;letter-spacing:-.035em}.hero h2{font-size:18px;font-weight:500;color:#aeb7c5;margin:0 0 22px}.hero p{max-width:790px;font-size:17px;line-height:1.65;color:#929cab}.actions{display:flex;gap:10px;margin-top:28px}.actions a,.card a,.observer a{display:inline-block;color:#a9c8ff;text-decoration:none;border:1px solid #303947;border-radius:7px;padding:9px 12px;font-size:12px}.actions .primary{background:#e9edf4;color:#0a0d12;border-color:#e9edf4}.principle{margin:26px 0 52px;padding:22px;background:#0d1118;border:1px solid #202630;border-radius:12px}.principle>span{display:block;font-size:10px;letter-spacing:.13em;color:#768193;font-weight:800}.principle strong{display:block;font-size:19px;margin:8px 0}.principle p{margin:0;color:#8994a5}.sectionHead{display:flex;justify-content:space-between;gap:32px;align-items:end;margin-bottom:18px}.sectionHead h2,.architecture h2,.observer h2{margin:8px 0 0;font-size:25px}.sectionHead p{max-width:460px;color:#838e9f;font-size:13px;line-height:1.5}.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.card{background:#0d1118;border:1px solid #202630;border-radius:12px;padding:22px}.card h3{font-size:23px;margin:8px 0 10px}.card>p{color:#939dac;line-height:1.55;min-height:74px}.boundary{background:#101620;border-left:2px solid #687588;padding:12px;margin:18px 0}.boundary b{display:block;font-size:10px;letter-spacing:.1em;color:#798597;margin-bottom:6px}.boundary span{font-size:12px;line-height:1.45;color:#bcc5d1}.architecture{margin-top:58px;padding-top:30px;border-top:1px solid #202630}.lanes{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:20px}.lanes div{padding:17px;border:1px solid #1e2530;border-radius:9px}.lanes b{display:block;margin-bottom:6px}.lanes span{font-size:12px;color:#8490a0}.observer{margin-top:42px;background:#0d1118;border:1px solid #263141;border-radius:12px;padding:24px;display:flex;justify-content:space-between;gap:30px;align-items:center}.observer p{max-width:700px;color:#8d98a8;line-height:1.55}.observer a{white-space:nowrap}footer{text-align:center;color:#525c69;font-size:10px;margin-top:42px}@media(max-width:760px){.hero h1{font-size:36px}.cards,.lanes{grid-template-columns:1fr}.sectionHead,.observer{display:block}.observer a{margin-top:12px}.card>p{min-height:0}}`}</style>
  </>
);

export default Home;
