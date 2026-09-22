from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as E
from PIL import Image,ImageDraw
from io import BytesIO
b=Path(r'C:/Users/kiden/OneDrive - University of Hartford/Documents/Hartford Assignments/.Current_Semester 9')
out=Path('.review/comsol');out.mkdir(exist_ok=True);imgs=[]
for k,p in enumerate(sorted(b.glob('*.docx'))):
 with ZipFile(p) as z:
  text=' '.join(E.fromstring(z.read('word/document.xml')).itertext());(out/f'report{k}.txt').write_text(text,encoding='utf8');print(k,p.name,text[:6000])
  for n in z.namelist():
   if n.startswith('word/media/'):
    try:
     original=Image.open(BytesIO(z.read(n))).convert('RGBA');im=Image.new('RGB',original.size,'white');im.paste(original,mask=original.getchannel('A'));name=f'comsol{k}-'+Path(n).stem+'.jpg';im.save(out/name);imgs.append((name,im))
    except Exception:pass
sheet=Image.new('RGB',(1000,210*((len(imgs)+3)//4)),'#182127');d=ImageDraw.Draw(sheet)
for i,(name,im) in enumerate(imgs):
 im.thumbnail((240,180));x=i%4*250;y=i//4*210;sheet.paste(im,(x,y));d.text((x,y+183),name,fill='white')
sheet.save(out/'contact.jpg')

