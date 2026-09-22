from pathlib import Path
from zipfile import ZipFile
import json
from PIL import Image, ImageOps, ImageDraw

base=Path(r'C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments')
out=Path(__file__).resolve().parents[1]/'.review'
out.mkdir(exist_ok=True)
sources={
 'monorail':base/'.LEGACY CLASSES/Semester 6/Mechatron/Project/gyro_scooter_project_Final.pptx',
 'arsh':base/'.LEGACY CLASSES/Semester 4/ENGR By Design/AR Smart headset A.R.S.H..pptx',
 'arsh-progress':base/'.LEGACY CLASSES/Semester 4/ENGR By Design/Progress Presentation2.pptx',
 'hsr':base/'.LEGACY CLASSES/Semester 1/ES 143/Expo Presentation/ES143_44470_ExpoPresentation_T4_95.pptx',
}
items=[]
for group,source in sources.items():
 with ZipFile(source) as z:
  for n in z.namelist():
   if n.startswith('ppt/media/') and n.lower().endswith(('.png','.jpg','.jpeg')):
    dest=out/f'{group}-{Path(n).name}'
    dest.write_bytes(z.read(n))
    im=Image.open(dest)
    if im.width<100 or im.height<100: continue
    items.append({'id':dest.name,'source':str(source),'entry':n,'path':str(dest),'size':im.size})
for source in sorted((base/'RockSat-C/Testing').glob('*')):
 if source.suffix.lower() in ('.jpg','.png','.jpeg'):
  im=Image.open(source)
  items.append({'id':'rocksat-'+source.name,'source':str(source),'path':str(source),'size':im.size})
for page in range(0,len(items),24):
 chunk=items[page:page+24]
 sheet=Image.new('RGB',(1200,((len(chunk)+3)//4)*230),'#182127')
 draw=ImageDraw.Draw(sheet)
 for i,item in enumerate(chunk):
  im=ImageOps.exif_transpose(Image.open(item['path'])).convert('RGB')
  im.thumbnail((285,192))
  x=(i%4)*300;y=(i//4)*230
  sheet.paste(im,(x+(300-im.width)//2,y))
  draw.text((x+8,y+197),item['id'],fill='white')
  draw.text((x+8,y+213),str(item['size']),fill='#b4bdc7')
 sheet.save(out/f'contact-{page//24+1}.jpg')
(out/'media.json').write_text(json.dumps(items,indent=2))
print(json.dumps({'count':len(items),'sheets':str(out/'contact-*.jpg')},indent=2))
