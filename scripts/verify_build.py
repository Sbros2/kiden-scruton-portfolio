from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import csv

root=Path(__file__).resolve().parents[1]/'dist'
errors=[];refs=0
class Page(HTMLParser):
 def handle_starttag(self,tag,attrs):
  global refs
  a=dict(attrs)
  for key in ['href','src','poster']:
   url=a.get(key,'')
   if not url.startswith('/') or url.startswith('//'):continue
   path=root/unquote(urlsplit(url).path).lstrip('/')
   if not path.is_file() and not (path/'index.html').is_file(): errors.append((str(self.file.relative_to(root)),url))
   refs+=1
  if tag=='img' and 'alt' not in a: errors.append((str(self.file),'missing alt'))
pages=list(root.rglob('*.html'))
for file in pages:
 p=Page();p.file=file;p.feed(file.read_text(encoding='utf-8'))
with (root/'assets/results/reference-acceleration.csv').open() as f: rows=list(csv.DictReader(f))
assert len(rows)==13577
assert abs((float(rows[-1]['timestamp_ms'])-float(rows[0]['timestamp_ms']))/1000-496.239)<1e-8
assert not errors,errors
print(f'PASS: {len(pages)} pages; {refs} internal links/media references; image alt attributes; 13,577 reference rows and exact duration.')
