"""QuantumScience Claw project page: owner-supplied research snapshot."""
from html import escape as esc
from pathlib import Path
from artifacts import render_artifacts

def project_page(link,hero,section,read):
 d=read('quantum_claw')
 def heading(title):return f'<div class="section-heading"><h2>{esc(title)}</h2></div>'
 def table(headers,rows,caption):
  return '<div class="blog-table"><table><caption>'+esc(caption)+'</caption><thead><tr>'+''.join(f'<th scope="col">{esc(h)}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+esc(row[0])+'</th>'+''.join('<td>'+esc(x)+'</td>' for x in row[1:])+'</tr>' for row in rows)+'</tbody></table></div>'
 overview=f'<div class="detail-grid"><div class="prose"><div class="eyebrow">Research question</div><h2>{esc(d["question"])}</h2><p>A locally deployed language-model agent coordinates specialized software for quantum error correction. Mathematical and numerical checks assess the produced artifacts separately from the agent’s final answer.</p><div class="actions"><a class="button" href="{link("blogs/quantumscience-claw-verifiable-science/")}">Read the research story →</a></div></div><aside class="metadata"><span class="label">Ongoing research</span><h3 style="margin-top:17px">Research leads</h3><p><strong>Ethan Seefried</strong><br><strong>Tirthankar Ghosal</strong></p><p class="resource-pending">{esc(d["publication"])}</p></aside></div>'
 layers='<div class="community-grid">'+''.join(f'<article class="community-card"><span class="label">Separate checkpoint</span><h3>{esc(s["title"])}</h3><p>{esc(s["body"])}</p></article>' for s in d['layers'])+'</div>'
 figure=f'<figure class="cosmo-figure"><a href="{link("assets/qsc-workflow.svg")}"><img src="{link("assets/qsc-workflow.svg")}" alt="Research question to local agent, typed operation, controlled execution, scientific verification, and accepted submission"></a><figcaption>Conceptual illustration based on the project team’s research narrative. These are independently observable stages.</figcaption></figure>'
 architecture=table(['Component','Current implementation'],[[x['component'],x['detail']] for x in d['architecture']],'Implementation described in the supplied evaluation snapshot.')
 benchmarks=table(['Workload','Outcome','Scope'],d['benchmarks'],'Results supplied by the project team; credited completion and verified scientific evidence are distinct.')
 failures=table(['Outcome among the 63 unfinished B1 tasks','Tasks'],d['b1_failures'],'B1 evaluation: 192 tasks, 14 code families, 300-second deadline per task.')
 limits='<div class="prose"><ul>'+''.join(f'<li>{esc(x)}</li>' for x in d['limitations'])+'</ul></div>'
 latency=f'<div class="notice">Local deployment snapshot: median inference request 22.7 s (450 requests); median worker process 0.49 s (74 processes); median complete episode approximately 134 s (68 episodes). {esc(d["latency"]["note"])}</div>'
 return hero('QuantumScience Claw (QSC)',d['summary'],link,('research/quantum/','Quantum research'))+section(overview)+section(heading('Three layers of reliability')+layers)+section(figure)+section(heading('Current system')+architecture)+section(heading('Evaluation snapshot')+benchmarks)+section(heading('Where task completion still falls short')+failures)+section(heading('What the evidence does—and does not—show')+limits+latency)+section(render_artifacts(Path(__file__).resolve().parent,d['slug'],link))
