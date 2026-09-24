import type { NextPage } from 'next';
import Head from 'next/head';

const systems = [
  {
    name: 'DGAF',
    type: 'Agentic governance / experimental control plane',
    description: 'Dynamic Governance Agentic Formation separates capability, evidence, verification, authority, and permission to act in governed multi-agent systems.',
    boundary: 'Track A Epoch 002 is closed for its exact preregistered scope. Scientific-N increment remains 0; canonical efficacy, independent validation, production certification, and High-Assurance authorization remain NOT ESTABLISHED / NOT AUTHORIZED.',
    href: 'https://github.com/ndrorchestration/DGAF-Framework',
  },
  {
    name: 'Orbit-Driftwatch',
    type: 'Multi-agent evaluation / observability',
    description: 'Observable role-separated workflows with source-aware provenance, disagreement and evidence-coverage metrics, portable run artifacts, and fail-closed claim auditing.',
    boundary: 'Deterministic controls and repository invariants are tested. Live hosted provider execution/retrieval is outside the currently verified public evidence boundary.',
    href: 'https://github.com/ndrorchestration/Orbit-Driftwatch',
  },
  {
    name: 'Collabration',
    type: 'Governed human + AI collaboration',
    description: 'A social application exploring accountable human/AI interaction with deny-by-default capability decisions, human approval gates, provenance, governed action records, and correction paths.',
    boundary: 'Independent product and evidence domain. DGAF patterns may inform the design without transferring DGAF authority, validation, or scientific claims.',
    href: 'https://github.com/ndrorchestration/Intellectro',
  },
  {
    name: 'Agent Control Plane',
    type: 'Control-plane primitives',
    description: 'A compact executable kernel for capability dispatch, explicit policy allow/deny decisions, cooperative execution budgets, and run-scoped provenance.',
    boundary: 'Tested local software invariants do not establish production security, distributed reliability, or autonomous-system certification.',
    href: 'https://github.com/ndrorchestration/agent-control-plane',
  },
  {
    name: 'AI Prompt Systems Portfolio',
    type: 'Prompt engineering / evaluation specifications',
    description: 'Public prompt-system artifacts covering state anchoring, constraint gates, multi-agent role decomposition, parametric behavior, and failure-aware recovery.',
    boundary: 'Checked-in prompt and evaluation specifications are artifacts, not evidence that a benchmark executed or that a model performs generally.',
    href: 'https://github.com/ndrorchestration/ai-prompt-systems-portfolio',
  },
];

const Home: NextPage = () => (
  <>
    <Head>
      <title>NDR AI Systems — Andrew Hensel</title>
      <meta name="description" content="AI systems design, evaluation, agentic governance, provenance, and orchestration by Andrew Hensel." />
    </Head>
    <main className="shell">
      <header className="hero">
        <span className="eyebrow">NDR AI SYSTEMS</span>
        <h1>Andrew “Ndr / Ender” Hensel</h1>
        <h2>AI Systems Design · Evaluation · Agentic Governance · Provenance</h2>
        <p>I design and evaluate AI systems around a practical question: what did the system actually do, what evidence supports that claim, and what is it authorized to do next?</p>
        <div className="actions">
          <a className="primary" href="https://github.com/ndrorchestration">GitHub</a>
          <a href="/orbit">Open ORBIT evidence observer</a>
        </div>
      </header>

      <section className="principle">
        <span>WORKING PRINCIPLE</span>
        <strong>Build the apparatus before claiming the result.</strong>
        <p>Capability, implementation, testing, verification, authorization, execution, and empirical support are kept as distinct evidence states.</p>
      </section>

      <section>
        <div className="sectionHead">
          <div><span className="eyebrow">SELECTED WORK</span><h2>Current portfolio systems</h2></div>
          <p>This is a curated professional surface, not the complete repository inventory. Each project keeps its own implementation and evidence authority.</p>
        </div>
        <div className="cards">
          {systems.map(system => (
            <article className="card" key={system.name}>
              <span className="type">{system.type}</span>
              <h3>{system.name}</h3>
              <p>{system.description}</p>
              <div className="boundary"><b>Evidence boundary</b><span>{system.boundary}</span></div>
              <a href={system.href}>View project →</a>
            </article>
          ))}
        </div>
      </section>

      <section className="architecture">
        <div><span className="eyebrow">PORTFOLIO ARCHITECTURE</span><h2>Research and engineering focus</h2></div>
        <div className="lanes">
          <div><b>Evaluation</b><span>Orbit-Driftwatch · negative controls · evidence classes · failure-mode discovery</span></div>
          <div><b>Governance</b><span>DGAF · evidence gates · provenance · authorization boundaries</span></div>
          <div><b>Orchestration</b><span>role separation · handoffs · control-plane design · cooperative budgets</span></div>
          <div><b>Prompt systems</b><span>state anchoring · constraint gates · structured outputs · failure-aware iteration</span></div>
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

      <footer>Curated public portfolio · project repositories and runtime providers remain authoritative for their own implementation, evidence, governance, and scientific state.</footer>
    </main>
    <style jsx global>{`*{box-sizing:border-box}body{margin:0;background:#07090d;color:#edf0f5;font-family:Inter,ui-sans-serif,system-ui,-apple-system,sans-serif}.shell{max-width:1180px;margin:auto;padding:58px 28px 46px}.eyebrow,.type{font-size:11px;letter-spacing:.14em;font-weight:800;color:#7e8999}.hero{padding:32px 0 48px;border-bottom:1px solid #202630}.hero h1{font-size:48px;line-height:1.05;margin:12px 0 8px;letter-spacing:-.035em}.hero h2{font-size:18px;font-weight:500;color:#aeb7c5;margin:0 0 22px}.hero p{max-width:790px;font-size:17px;line-height:1.65;color:#929cab}.actions{display:flex;gap:10px;margin-top:28px}.actions a,.card a,.observer a{display:inline-block;color:#a9c8ff;text-decoration:none;border:1px solid #303947;border-radius:7px;padding:9px 12px;font-size:12px}.actions .primary{background:#e9edf4;color:#0a0d12;border-color:#e9edf4}.principle{margin:26px 0 52px;padding:22px;background:#0d1118;border:1px solid #202630;border-radius:12px}.principle>span{display:block;font-size:10px;letter-spacing:.13em;color:#768193;font-weight:800}.principle strong{display:block;font-size:19px;margin:8px 0}.principle p{margin:0;color:#8994a5}.sectionHead{display:flex;justify-content:space-between;gap:32px;align-items:end;margin-bottom:18px}.sectionHead h2,.architecture h2,.observer h2{margin:8px 0 0;font-size:25px}.sectionHead p{max-width:460px;color:#838e9f;font-size:13px;line-height:1.5}.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.card{background:#0d1118;border:1px solid #202630;border-radius:12px;padding:22px}.card h3{font-size:23px;margin:8px 0 10px}.card>p{color:#939dac;line-height:1.55;min-height:74px}.boundary{background:#101620;border-left:2px solid #687588;padding:12px;margin:18px 0}.boundary b{display:block;font-size:10px;letter-spacing:.1em;color:#798597;margin-bottom:6px}.boundary span{font-size:12px;line-height:1.45;color:#bcc5d1}.architecture{margin-top:58px;padding-top:30px;border-top:1px solid #202630}.lanes{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:20px}.lanes div{padding:17px;border:1px solid #1e2530;border-radius:9px}.lanes b{display:block;margin-bottom:6px}.lanes span{font-size:12px;color:#8490a0}.observer{margin-top:42px;background:#0d1118;border:1px solid #263141;border-radius:12px;padding:24px;display:flex;justify-content:space-between;gap:30px;align-items:center}.observer p{max-width:700px;color:#8d98a8;line-height:1.55}.observer a{white-space:nowrap}footer{text-align:center;color:#525c69;font-size:10px;margin-top:42px}@media(max-width:760px){.hero h1{font-size:36px}.cards,.lanes{grid-template-columns:1fr}.sectionHead,.observer{display:block}.observer a{margin-top:12px}.card>p{min-height:0}}`}</style>
  </>
);

export default Home;
