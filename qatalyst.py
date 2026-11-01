"""Shared visual project and story layout for Qatalyst."""
from html import escape as esc

def render(l,hero,section,read,project=False):
 post=next(p for p in read('blogs') if p['slug']=='qatalyst-algorithm-discovery-for-science')
 repo=post['github_url']; parts=post['sections']
 def figure(f):
  return f'<figure class="qatalyst-figure"><a href="{l(f["path"])}"><img src="{l(f["path"])}" alt="{esc(f["alt"])}"></a><figcaption>{esc(f["caption"])} <a href="{esc(f["source"])}">{esc(f["source_label"])} ↗</a></figcaption></figure>'
 intro=f'<div class="qatalyst-intro"><div><span class="label">MIT Science Hackathon · Autonomous science</span><h2>{esc(parts[0]["heading"])}</h2><p>{esc(parts[0]["body"])}</p></div><aside class="qatalyst-team"><span class="label">Built by</span><p>Sanjay Das · Ethan Seefried · Chris · Tahisha · Shaziaviedi</p><div class="actions"><a class="button" href="{repo}">Explore the code ↗</a><a class="button secondary" href="{repo}/blob/main/docs/architecture.md">Architecture ↗</a></div></aside></div>'
 body=intro+figure(post['figures'][0])
 body+='<div class="qatalyst-metrics">'+''.join(f'<div><strong>{value}</strong><span>{label}</span></div>' for value,label in [('96','papers in completed Sonnet study'),('93 / 96','A2m circuits reached simulation'),('28 / 28','affine pilot instances checked'),('15 / 21','partial hybrid reviewed-ready')])+'</div>'
 body+='<nav class="qatalyst-nav" aria-label="On this page"><a href="#q-1">Architecture</a><a href="#q-3">Benchmark</a><a href="#q-4">Examples</a><a href="#q-9">Mission & next steps</a></nav>'
 for i,s in enumerate(parts[1:],1):
  body+=f'<section class="qatalyst-section" id="q-{i}"><div class="qatalyst-section-label"><span class="label">{i:02d} / {"Research direction" if i>=9 else "Inside Qatalyst"}</span><h2>{esc(s["heading"])}</h2></div><div class="qatalyst-copy"><p>{esc(s["body"])}</p>'
  if i==3:
   t=post['results']; body+='<div class="blog-table"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(x)+'</th>' for x in t['headers'])+'</tr></thead><tbody>'
   for row in t['rows']:body+='<tr><th scope="row">'+esc(row[0])+'</th>'+''.join('<td>'+esc(x)+'</td>' for x in row[1:])+'</tr>'
   body+='</tbody></table></div>'
  if i==4:body+=figure(post['figures'][1])
  if i==5:body+='<div class="qatalyst-rule"><span>Hidden rule</span><strong>f(x) = a·x ⊕ b</strong><span>Reconstruct → simulate → check a and b</span><p>28 tested instances · 1–3 data qubits · explicit oracle assumptions</p></div>'
  body+='</div></section>'
 body+=f'<div class="qatalyst-closing"><span class="label">Build the next experiment with us</span><h2>Bring a question worth testing.</h2><div class="actions"><a class="button" href="{repo}">Code & experimental artifacts ↗</a><a class="button secondary" href="{l("research/autonomous/")}">Explore autonomous science →</a><a class="button secondary" href="{l("contact/")}">Connect with SI² →</a></div></div><aside class="notice">{esc(post["source_note"])}</aside>'
 title='Algorithm Discovery for Science' if project else post['title']
 return '<div class="qatalyst-page">'+hero(title,post['summary'],l,('projects/' if project else 'blogs/','Projects' if project else 'Stories'))+section(body)+'</div>'
