import type { NextPage } from 'next';
import Head from 'next/head';

const links = [
  {
    label: 'AOGA Dashboard',
    href: 'https://aoga-dashboard.vercel.app',
    description: 'Live real-time AI governance metrics & agent monitoring',
    tag: 'Live',
  },
  {
    label: 'GitHub — ndrorchestration',
    href: 'https://github.com/ndrorchestration',
    description: 'DGAF-Framework, Driftwatch, sentinel-governance & all repos',
    tag: 'Code',
  },
  {
    label: 'Needle.app Templates',
    href: 'https://needle.app/partners-directory/ndr-ai-orchestration',
    description: 'Published AI governance & evaluation workflow templates',
    tag: 'Templates',
  },
  {
    label: 'LinkedIn',
    href: 'https://linkedin.com/in/andrewhensel',
    description: 'Andrew // Ndr \'Ender\' Hensel — AI orchestration & governance',
    tag: 'Connect',
  },
];

const Home: NextPage = () => {
  return (
    <>
      <Head>
        <title>NDR Orchestration — AI Governance Ecosystem</title>
        <meta name="description" content="AI governance, multi-agent orchestration, and evaluation infrastructure by Andrew Hensel (NDR Orchestration)." />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main style={{
        minHeight: '100vh',
        background: '#0a0a0a',
        color: '#e5e5e5',
        fontFamily: 'system-ui, -apple-system, sans-serif',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem',
      }}>
        <div style={{ maxWidth: '680px', width: '100%' }}>
          <header style={{ marginBottom: '3rem', textAlign: 'center' }}>
            <p style={{ color: '#7c6af7', fontWeight: 600, letterSpacing: '0.08em', fontSize: '0.8rem', textTransform: 'uppercase', marginBottom: '0.75rem' }}>
              NDR Orchestration
            </p>
            <h1 style={{ fontSize: '2rem', fontWeight: 700, margin: '0 0 1rem', lineHeight: 1.2 }}>
              AI Governance Ecosystem
            </h1>
            <p style={{ color: '#888', fontSize: '0.95rem', lineHeight: 1.6, margin: 0 }}>
              Institutional-grade evaluation pipelines, multi-agent orchestration,
              and the DGAF (Dynamic Governance Agentic Formation) framework.
            </p>
          </header>

          <nav>
            {links.map((link) => (
              <a
                key={link.href}
                href={link.href}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'flex-start',
                  padding: '1.1rem 1.25rem',
                  marginBottom: '0.75rem',
                  background: '#141414',
                  border: '1px solid #222',
                  borderRadius: '10px',
                  textDecoration: 'none',
                  color: 'inherit',
                  transition: 'border-color 0.15s',
                  cursor: 'pointer',
                }}
              >
                <div>
                  <div style={{ fontWeight: 600, marginBottom: '0.25rem' }}>{link.label}</div>
                  <div style={{ fontSize: '0.85rem', color: '#777' }}>{link.description}</div>
                </div>
                <span style={{
                  fontSize: '0.7rem',
                  fontWeight: 600,
                  background: '#1e1a3a',
                  color: '#9d8bfa',
                  padding: '0.25rem 0.6rem',
                  borderRadius: '4px',
                  whiteSpace: 'nowrap',
                  marginLeft: '1rem',
                  marginTop: '2px',
                }}>
                  {link.tag}
                </span>
              </a>
            ))}
          </nav>

          <footer style={{ marginTop: '3rem', textAlign: 'center', color: '#444', fontSize: '0.8rem' }}>
            DGAF Framework · Phi-Calculus Architecture · Agent Amethyst meta-orchestrated
          </footer>
        </div>
      </main>
    </>
  );
};

export default Home;
