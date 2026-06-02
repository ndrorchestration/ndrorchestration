import Link from 'next/link';
import { useRouter } from 'next/router';
import { ReactNode } from 'react';

const NAV_ITEMS = [
  { label: 'Overview', href: '/' },
];

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  const router = useRouter();
  return (
    <div>
      <nav>
        {NAV_ITEMS.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            style={{ marginRight: '1rem', fontWeight: router.pathname === item.href ? 700 : 400 }}
          >
            {item.label}
          </Link>
        ))}
      </nav>
      <main>{children}</main>
    </div>
  );
}
