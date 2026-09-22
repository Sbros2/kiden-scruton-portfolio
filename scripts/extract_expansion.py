from pathlib import Path
from zipfile import ZipFile
from PIL import Image,ImageDraw
from io import BytesIO
b=Path(r'C:/Users/kiden/OneDrive - University of Hartford/Documents/Hartford Assignments/.LEGACY CLASSES/Semester 7')
out=Path('.review/expansion');imgs=[]
groups={'fan':b/'CAD/Fan Project/Final Submission/Technical Report For Fan Project.docx','aero':b/'aero/Aero Proj/Aero Proj/Aerodynamics Project2.docx'}
for g,p in groups.items():
 with ZipFile(p) as z:
  for n in z.namelist():
   if n.startswith('word/media/'):
    try:
     im=Image.open(BytesIO(z.read(n))).convert('RGB');name=g+'-'+Path(n).stem+'.jpg';im.save(out/name);imgs.append((name,im))
    except Exception:pass
sheet=Image.new('RGB',(1000,210*((len(imgs)+3)//4)),'#182127');d=ImageDraw.Draw(sheet)
for i,(name,im) in enumerate(imgs):
 im.thumbnail((240,180));x=i%4*250;y=i//4*210;sheet.paste(im,(x,y));d.text((x,y+183),name,fill='white')
sheet.save(out/'contact.jpg')
