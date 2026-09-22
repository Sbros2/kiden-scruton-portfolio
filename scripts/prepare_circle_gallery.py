from pathlib import Path
from PIL import Image,ImageDraw
import shutil
base=Path(r'C:/Users/kiden/OneDrive - University of Hartford/Documents/Hartford Assignments/.LEGACY CLASSES/Semester 6/Circ Invert project/Presentation')
items={'circle-two':'circle_inversion_between_two_circles.gif','circle-trace':'circle_inversion_with_angle_and_3pt_trace.gif','circle-periodic':'algo1_4circles_ABCD.gif','circle-random':'algo4_4circles_fully_random.gif','circle-line':'Line-detacted-inv.png','circle-arc':'Arc_to_Circle.png'}
sheet=Image.new('RGB',(900,500),'#182127');d=ImageDraw.Draw(sheet)
for i,(name,source) in enumerate(items.items()):
 p=base/source;shutil.copy2(p,Path('public/assets')/(name+p.suffix))
 im=Image.open(p);im.seek(getattr(im,'n_frames',1)//2);im=im.convert('RGB');im.thumbnail((290,210));x=i%3*300;y=i//3*250;sheet.paste(im,(x,y));d.text((x,y+215),name,fill='white')
sheet.save('.review/circle-gallery.jpg')
shutil.copy2(base/'FinalcirclesSP25.pptx','public/documents/circle-inversions-final.pptx')
