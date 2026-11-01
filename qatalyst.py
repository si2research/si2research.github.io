"""A compact editorial layout for the Qatalyst project and research story."""
from html import escape as esc

def render(l,hero,section,read,project=False):
 post=next(p for p in read('blogs') if p['slug']=='qatalyst-algorithm-discovery-for-science')
 repo=post['github_url']
 def figure(f):
  return f'<figure class="qatalyst-figure"><a href="{l(f["path"])}"><img src="{l(f["path"])}" alt="{esc(f["alt"])}" loading="lazy"></a><figcaption>{esc(f["caption"])}</figcaption></figure>'
 body=f'<div class="qatalyst-byline">MIT Science Hackathon · {esc(post["reading_time"])}<br><span>Sanjay Das · Ethan Seefried · Chris · Tahisha · Shaziaviedi</span></div><div class="actions"><a class="button" href="{repo}">Explore the code ↗</a><a class="text-link" href="{repo}/blob/main/docs/architecture.md">Architecture notes ↗</a></div>'
 for i,s in enumerate(post['sections']):
  body+=f'<section class="qatalyst-chapter"><h2>{esc(s["heading"])}</h2><p>{esc(s["body"])}</p>'
  if i==1:
   body+='<div class="qatalyst-patterns">'
   for slug,title,desc in [('single','Single agent','One researcher carries the plan from abstract to implementation.'),('centralized','Centralized team','A lead agent assigns work and combines the workers’ results.'),('decentralized','Ledger-coordinated team','Agents select and share work through a common task board.')]:
    body+=f'<figure><img src="{l("assets/blog/qatalyst-"+slug+".svg")}" alt="{esc(desc)}"><figcaption><strong>{title}</strong><span>{desc}</span></figcaption></figure>'
   body+='<p class="qatalyst-diagram-note">Conceptual patterns. Shared state can decentralize work selection while infrastructure remains centralized.</p></div>'
  if i==2:
   body+='<ol class="qatalyst-game"><li><strong>Propose</strong><span>Record a candidate and its assumptions.</span></li><li><strong>Test & review</strong><span>Execute the code; challenge the result.</span></li><li><strong>Reward or revise</strong><span>Credit progress after execution and review.</span></li><li><strong>Replace & vary</strong><span>At zero energy, replace within budget.</span></li></ol><p class="qatalyst-diagram-note">An illustrative lifecycle for the native hybrid. Energy is a virtual budget; survival advantage has not been established.</p>'
  for f in post['figures']:
   if f['after_section']==i:body+=figure(f)
  if i==5:
   t=post['results']; body+='<div class="blog-table"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'
   for row in t['rows']:body+='<tr><th scope="row">'+esc(row[0])+'</th>'+''.join('<td>'+esc(x)+'</td>' for x in row[1:])+'</tr>'
   body+='</tbody></table></div>'
  body+='</section>'
 body+=f'<div class="qatalyst-end"><a class="button" href="{repo}">Explore code & experiments ↗</a><a class="text-link" href="{l("research/autonomous/")}">Autonomous science at SI² →</a></div><aside class="qatalyst-footnote"><h2>Team & support</h2><p>{esc(read("qatalyst_credits")["text"])}</p><p>{esc(post["source_note"])}</p></aside>'
 return '<div class="qatalyst-page qatalyst-editorial">'+hero('Algorithm Discovery for Science' if project else post['title'],post['summary'],l,('projects/' if project else 'blogs/','Projects' if project else 'Stories'))+section('<article class="qatalyst-article">'+body+'</article>')+'</div>'
