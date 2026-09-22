from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parents[1]
academic=Path(r'C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments')
piezo=Path(r'C:\Users\kiden\Documents\.ACTUAL DOCS\Kiden\Code And Personal Proj\Piezo Circ')
sources={
 'piezo-testing':piezo/'Final Draft/Pspice Testing.docx',
 'piezo-proposal':piezo/'Piezo Electric Harvester/Piezoelectric Energy Proposal.docx',
 'monorail-model':academic/'.LEGACY CLASSES/Semester 6/Mechatron/Project/ME 505 Modeling Report.docx',
 'monorail-report':academic/'.LEGACY CLASSES/Semester 6/Mechatron/Project/Gyroscopic Scooter 405.docx',
 'hsr-report':academic/'.LEGACY CLASSES/Semester 1/ES 143/Expo Report/ES143_44470_T4_HazardSensingRobot_Final.docx',
 'arsh-report':academic/'.LEGACY CLASSES/Semester 4/ENGR By Design/HSB and IoT Presentation Report.docx',
 'rocksat-writeup':academic/'RockSat-C/Write-Up Kiden Scruton 1_24.docx',
}
out=root/'.review/documents';out.mkdir(exist_ok=True)
for key,path in sources.items():
 with ZipFile(path) as z:
  tree=ET.fromstring(z.read('word/document.xml'))
  text='\n'.join(''.join(p.itertext()) for p in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
  (out/f'{key}.txt').write_text(text,encoding='utf-8')
  imgs=[]
  for name in z.namelist():
   if name.startswith('word/media/'):
    dest=out/f'{key}-{Path(name).name}';dest.write_bytes(z.read(name))
    try:
     im=Image.open(dest)
     if im.width>200 and im.height>100:imgs.append(dest)
    except Exception:pass
  if imgs:
   sheet=Image.new('RGB',(1200,((len(imgs)+3)//4)*230),'#e8eeee');draw=ImageDraw.Draw(sheet)
   for i,p in enumerate(imgs):
    im=ImageOps.contain(Image.open(p).convert('RGB'),(290,195));x=i%4*300;y=i//4*230
    sheet.paste(im,(x,y));draw.text((x,y+200),p.name.replace(key+'-',''),fill='black')
   sheet.save(out/f'{key}-contact.jpg')
  print(key,len(text),'characters;',len(imgs),'figures')
