"""Project page for the owner-supplied COSMOAGENT research."""
from html import escape as esc
from pathlib import Path
from artifacts import render_artifacts

def project_page(link,hero,section,read):
 d=read('cosmology')
 def heading(title):return f'<h2>{esc(title)}</h2>'
 leaders=''.join(f'<li><strong>{esc(p["name"])}</strong> — {esc(p["role"])}</li>' for p in d['leadership'])
 milestones=''.join(f'<li>{esc(s)}</li>' for s in d['achievements'])
 diagram=f'<figure class="cosmo-figure"><img src="{link("assets/cosmoagent-workflow.svg")}" alt="COSMOAGENT: scientist sets a goal, agents plan, run, debug, and analyze simulations on Frontier"><figcaption>Workflow illustration based on the project team’s supplied slides.</figcaption></figure>'
 overview=f'<div class="detail-grid"><div class="prose"><div class="eyebrow">The research question</div><h2>{esc(d["question"])}</h2><p>{esc(d["goal"])}</p><h2>From a question to an experiment</h2><p>{esc(d["approach"])}</p></div><aside class="metadata"><span class="label">COSMOAGENT</span><h3 style="margin-top:15px">Project information</h3><dl><dt>Program</dt><dd>{esc(d["program"])}</dd><dt>Computing platform</dt><dd>Frontier</dd><dt>Research directions</dt><dd>AI for HPC · Autonomous scientific discovery</dd><dt>Publication</dt><dd>{esc(d["publication"])}</dd></dl></aside></div>'
 results=f'<div class="prose"><h2>Demonstrated milestones</h2><ul>{milestones}</ul><div class="notice">{esc(d["scope_note"])}</div></div>'
 team=f'<div class="community-grid"><article class="community-card"><span class="label">Project leadership</span><h3>Scientific direction</h3><ul>{leaders}</ul></article><article class="community-card"><span class="label">Research members</span><h3>Agentic simulation team</h3><p>{esc(", ".join(d["members"]))}</p></article><article class="community-card"><span class="label">Collaborating institutions</span><h3>Across disciplines</h3><p>{esc(" · ".join(d["institutions"]))}</p></article></div>'
 recognition=f'<div class="blog-award-note"><span class="label">14th ORPA Symposium · ORNL</span><h2>1st Place Poster Award</h2><p>“{esc(d["poster"])}” received first-place poster recognition.</p><a class="text-link" href="{link("awards/")}">Awards & recognition →</a></div>'
 return hero(d['title'],'COSMOAGENT: toward autonomous cosmological discovery on Frontier.',link,('projects/','Projects'))+section(overview)+section(diagram)+section(results)+section(team)+section(recognition)+section(f'<div class="sponsor-ack"><span class="label">Program & support</span><h3>{esc(d["program"])}</h3><p>{esc(d["support"])}</p></div>')+section(render_artifacts(Path(__file__).resolve().parent,'agentic-cosmology',link))
