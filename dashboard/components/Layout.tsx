import Link from 'next/link';
import { useRouter } from 'next/router';
import { ReactNode } from 'react';

const NAV_ITEMS = [
  { label: 'Overview',      href: '/' },
  { label: 'Agent Roster',  href: '/agents' },
  { label: 'NDR Patterns',  href: '/patterns' },
  { label: 'Phi Monitor',   href: '/phi-monitor' },
  { label: 'Gate Demo',     href: '/gate-demo' },
  { label: 'Phi-Closure',   href: '/phi-closure' },
  { label: 'PDMAL',         href: '/pdmal' },
  { label: 'API Docs',      href: '/api-docs' },
];

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const router = useRouter();
  return (
    <div style={{ fontFamily: 'system-ui, -apple-system, sans-serif', minHeight: '100vh', background: '#0a0a0a', color: '#e5e5e5' }}>
      <nav style={{
        display: 'flex',
        gap: '0.25rem',
        padding: '0.75rem 1.5rem',
        borderBottom: '1px solid #1e1e1e',
        flexWrap: 'wrap',
      }}>
        {NAV_ITEMS.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            style={{
              padding: '0.35rem 0.75rem',
              borderRadius: '6px',
              fontSize: '0.82rem',
              fontWeight: router.pathname === item.href ? 600 : 400,
              color: router.pathname === item.href ? '#9d8bfa' : '#888',
              background: router.pathname === item.href ? '#1e1a3a' : 'transparent',
              textDecoration: 'none',
              transition: 'color 0.15s, background 0.15s',
            }}
          >
            {item.label}
          </Link>
        ))}
      </nav>
      <main style={{ padding: '2rem 1.5rem' }}>{children}</main>
    </div>
  );
}
