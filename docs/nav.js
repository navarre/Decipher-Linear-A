/* Sidebar Navigation Component */
/* Load this on every page: <script src="nav.js"></script> */

(function() {
  const pages = [
    { id: 'home', label: 'Home', href: 'index.html', icon: '𐘇' },
    { id: 'browse', label: 'Browse Corpus', href: 'browse.html', icon: '📜' },
    { id: 'signs', label: 'Sign Catalog', href: 'signs.html', icon: '𐘀' },
    { id: 'terms', label: 'Terminology', href: 'terminology.html', icon: '📖' },
    { id: 'audit', label: 'Data Audit', href: 'discrepancies.html', icon: '🔍' }
  ];

  // Detect current page
  const path = window.location.pathname;
  const currentFile = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

  // Inject CSS
  const style = document.createElement('style');
  style.textContent = `
    .sidebar-nav {
      position: fixed;
      left: 0;
      top: 0;
      bottom: 0;
      width: 220px;
      background: #0d0d14;
      border-right: 1px solid var(--border, #2a2a3a);
      display: flex;
      flex-direction: column;
      z-index: 1000;
      transition: transform 0.25s ease;
    }
    .sidebar-brand {
      padding: 1.5rem 1.2rem 1rem;
      border-bottom: 1px solid var(--border, #2a2a3a);
    }
    .sidebar-brand a {
      color: var(--accent, #c49b5c);
      text-decoration: none;
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      display: block;
    }
    .sidebar-brand .brand-sub {
      color: var(--text2, #9090a0);
      font-size: 0.7rem;
      font-weight: 400;
      margin-top: 0.2rem;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .sidebar-links {
      flex: 1;
      padding: 0.8rem 0;
      overflow-y: auto;
    }
    .sidebar-links a {
      display: flex;
      align-items: center;
      gap: 0.7rem;
      padding: 0.6rem 1.2rem;
      color: var(--text2, #9090a0);
      text-decoration: none;
      font-size: 0.9rem;
      transition: all 0.15s;
      border-left: 3px solid transparent;
    }
    .sidebar-links a:hover {
      color: var(--text, #e0e0e8);
      background: rgba(255,255,255,0.03);
    }
    .sidebar-links a.active {
      color: var(--accent, #c49b5c);
      background: rgba(196,155,92,0.08);
      border-left-color: var(--accent, #c49b5c);
    }
    .sidebar-links .nav-icon {
      width: 1.4rem;
      text-align: center;
      font-size: 1rem;
    }
    .sidebar-footer {
      padding: 1rem 1.2rem;
      border-top: 1px solid var(--border, #2a2a3a);
      font-size: 0.7rem;
      color: var(--text2, #9090a0);
    }
    .sidebar-footer a {
      color: var(--accent, #c49b5c);
      text-decoration: none;
    }

    /* Push page content right */
    body { margin-left: 220px !important; }
    /* Hide old nav */
    body > nav { display: none !important; }

    /* Mobile: collapsible */
    .sidebar-toggle {
      display: none;
      position: fixed;
      top: 0.8rem;
      left: 0.8rem;
      z-index: 1001;
      background: var(--surface, #12121a);
      border: 1px solid var(--border, #2a2a3a);
      border-radius: 6px;
      color: var(--accent, #c49b5c);
      font-size: 1.3rem;
      padding: 0.4rem 0.6rem;
      cursor: pointer;
      line-height: 1;
    }
    @media (max-width: 768px) {
      .sidebar-nav { transform: translateX(-100%); }
      .sidebar-nav.open { transform: translateX(0); }
      .sidebar-toggle { display: block; }
      body { margin-left: 0 !important; }
      .sidebar-overlay {
        display: none;
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.5);
        z-index: 999;
      }
      .sidebar-overlay.open { display: block; }
    }
  `;
  document.head.appendChild(style);

  // Build sidebar HTML
  const sidebar = document.createElement('aside');
  sidebar.className = 'sidebar-nav';

  let linksHtml = '';
  for (const p of pages) {
    const isActive = currentFile === p.href || (currentFile === '' && p.href === 'index.html');
    linksHtml += `<a href="${p.href}"${isActive ? ' class="active"' : ''}><span class="nav-icon">${p.icon}</span>${p.label}</a>`;
  }

  sidebar.innerHTML = `
    <div class="sidebar-brand">
      <a href="index.html">Linear A<br>Research Project</a>
      <div class="brand-sub">Computational Corpus</div>
    </div>
    <div class="sidebar-links">${linksHtml}</div>
    <div class="sidebar-footer">
      <a href="https://github.com/navarre/minoan-linear-a">GitHub</a>
    </div>
  `;

  // Toggle button for mobile
  const toggle = document.createElement('button');
  toggle.className = 'sidebar-toggle';
  toggle.innerHTML = '☰';
  toggle.setAttribute('aria-label', 'Toggle navigation');

  // Overlay for mobile
  const overlay = document.createElement('div');
  overlay.className = 'sidebar-overlay';

  toggle.addEventListener('click', function() {
    sidebar.classList.toggle('open');
    overlay.classList.toggle('open');
  });
  overlay.addEventListener('click', function() {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
  });

  // Insert into DOM
  document.body.prepend(sidebar);
  document.body.prepend(overlay);
  document.body.prepend(toggle);
})();
