from pathlib import Path
import shutil

root = Path.cwd()
page = root / 'app/page.tsx'
css = root / 'app/globals.css'

if not page.exists() or not css.exists():
    raise SystemExit('Run this from the Next.js project root (where app/page.tsx and app/globals.css exist).')

page_text = page.read_text()
css_text = css.read_text()

if 'id="ambassador"' in page_text:
    raise SystemExit('Ambassador & Advocate Roles section is already in page.tsx. Nothing changed.')

page_backup = page.with_suffix('.tsx.ambassador-backup')
css_backup = css.with_suffix('.css.ambassador-backup')
shutil.copy2(page, page_backup)
shutil.copy2(css, css_backup)

section = r'''
<div className="section-wrap" id="ambassador">
<p className="section-label">Ambassador &amp; Advocate Roles</p>
<p className="section-sub">Onchain advocacy, ecosystem content, and <em>work that moved beyond the post.</em></p>

<div className="ambassador-project">
<div className="ambassador-project-head">
<div>
<p className="campaign-period">June 21 — August 1, 2026</p>
<h3 className="campaign-client">GoldRush <span className="project-powered">· powered by Covalent</span></h3>
<p className="campaign-brief">Structured onchain data API. Work included building dashboards, quoting official posts, writing Medium articles, and 20+ ecosystem replies daily.</p>
</div>
</div>
<div className="content-grid ambassador-grid">
<a className="content-card" href="https://x.com/favour_D_crier/status/2076520399634899390" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-sh-dashboard.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Dashboard</span></div><h3 className="card-title">SH Hynix Pre-IPO Dashboard</h3><p className="card-tagline">Dashboard work built around the SH Hynix pre-IPO market.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2077728698963231051" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-rwa-perps.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Dashboard</span></div><h3 className="card-title">RWA / Perps Dashboard</h3><p className="card-tagline">Market view covering RWA/Perps activity, winners, losers, and volume.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2070589267194122530" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-h3-pro.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Dashboard</span></div><h3 className="card-title">H3-Pro</h3><p className="card-tagline">Market dashboard covering funding, dominance, volume, and top movers.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2070228310655635956" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-whale-tracker.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Dashboard</span></div><h3 className="card-title">Whale Tracker</h3><p className="card-tagline">Hyperliquid whale tracking with accumulation trends and live position data.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2069167522574676017" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-explainer.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Explainer</span></div><h3 className="card-title">GoldRush: The Complete Data Layer for Hyperliquid</h3><p className="card-tagline">Visual explainer covering GoldRush's HyperCore and HyperEVM data layers.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2069037906287530262" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-spacex.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Research Post</span></div><h3 className="card-title">Who Actually Got Into Tokenized SpaceX?</h3><p className="card-tagline">A data-led look at the wallets and activity around tokenized SpaceX.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://medium.com/@favour_d_crier/best-multichain-blockchain-data-apis-in-2026-d3fd16dca369" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-multichain-apis.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Article</span></div><h3 className="card-title">Best Multichain Blockchain Data APIs in 2026</h3><p className="card-tagline">A developer's guide to multichain blockchain data APIs.</p><span className="card-cta">Read Article  →</span></div>
</a>
<a className="content-card" href="https://medium.com/@favour_d_crier/how-hyperliquid-turned-market-creation-into-a-meta-d44870346db0" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/goldrush-hyperliquid-meta.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Article</span></div><h3 className="card-title">How Hyperliquid Turned Market Creation Into A Meta</h3><p className="card-tagline">Exploring the market-creation meta around Hyperliquid.</p><span className="card-cta">Read Article  →</span></div>
</a>
</div>
<div className="ambassador-results">
<p className="results-label">Conversions</p>
<div className="results-grid">
<div><span className="results-num">32</span><span className="results-text">Sign-ups</span></div>
<div><span className="results-num">12</span><span className="results-text">Subscriptions</span></div>
<div><span className="results-num">30k+</span><span className="results-text">Post Impressions</span></div>
</div>
<p className="results-note">Targeted engagements from the Hyperliquid and RWA communities on top posts.</p>
</div>
</div>

<div className="ambassador-project">
<div className="ambassador-project-head">
<div>
<p className="campaign-period">August 5 — September 1, 2026</p>
<h3 className="campaign-client">Orion</h3>
<p className="campaign-brief">A reputation-verified marketplace and infrastructure layer for autonomous AI agents. Work included quoting official posts, quoting higher tiers, and building AI agents/bots.</p>
</div>
</div>
<div className="content-grid ambassador-grid">
<a className="content-card" href="https://x.com/favour_D_crier/status/2087753414641881166" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/orion-builder-hackathon.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Hackathon</span></div><h3 className="card-title">Orion Builder Hackathon</h3><p className="card-tagline">Content around Orion's $5,000 builder hackathon and creator reward pool.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2088006638535922101" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/orion-agent-store.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Product Launch</span></div><h3 className="card-title">Orion Agent Store</h3><p className="card-tagline">Breaking down the live agent marketplace: build, deploy, earn.</p><span className="card-cta">View Post  →</span></div>
</a>
<a className="content-card" href="https://x.com/favour_D_crier/status/2088459794277388592" target="_blank" rel="noreferrer">
<div className="card-img" style={{backgroundImage: "url('/assets/ambassador/orion-termux.jpg')"}}></div>
<div className="card-body"><div className="card-meta"><span className="card-type">Ecosystem</span></div><h3 className="card-title">Orion Partners With Termux</h3><p className="card-tagline">Content explaining how autonomous agents can find jobs, accept tasks, and work together.</p><span className="card-cta">View Post  →</span></div>
</a>
</div>
<div className="ambassador-results">
<p className="results-label">Conversions</p>
<div className="results-grid">
<div><span className="results-num">12</span><span className="results-text">$ORN Launch Investments</span></div>
<div><span className="results-num">20+</span><span className="results-text">Hackathon Sign-ups</span></div>
<div><span className="results-num">15k+</span><span className="results-text">Post Engagements</span></div>
</div>
</div>
</div>
</div>
'''

marker = '<div className="section-wrap" id="wins">'
if marker not in page_text:
    raise SystemExit('Could not find the Wins section marker in app/page.tsx; no changes made.')

page_text = page_text.replace(marker, section + '\n' + marker, 1)
page.write_text(page_text)

css_add = r'''

/* AMBASSADOR & ADVOCATE ROLES */
.ambassador-project{margin-top:3.5rem}
.ambassador-project+.ambassador-project{margin-top:5rem}
.ambassador-project-head{border-left:2px solid var(--accent);padding-left:1.5rem;margin-bottom:2rem}
.project-powered{font-family:"DM Mono",monospace;font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:300}
.ambassador-grid{margin-top:0}
.ambassador-results{margin-top:2.25rem;padding-top:1.5rem;border-top:1px solid var(--border)}
.results-label{font-size:.55rem;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);margin-bottom:1rem}
.results-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem}
.results-grid>div{border-left:1px solid var(--border);padding-left:1rem}
.results-num{display:block;font-family:"Cormorant Garamond",serif;font-size:2rem;font-weight:300;line-height:1;color:var(--text)}
.results-text{display:block;font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-top:.35rem}
.results-note{font-size:.62rem;line-height:1.7;color:var(--muted);margin-top:1rem;max-width:620px}
@media(max-width:560px){.results-grid{grid-template-columns:1fr;gap:1rem}.ambassador-project+.ambassador-project{margin-top:4rem}.project-powered{display:block;margin-top:.35rem}}
'''

css.write_text(css_text.rstrip() + css_add + '\n')
print('Applied Ambassador & Advocate Roles section before Wins.')
print(f'Backups: {page_backup.name}, {css_backup.name}')
