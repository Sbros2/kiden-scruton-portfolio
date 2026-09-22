from pathlib import Path
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
gif=Image.open(root/'public/assets/FTC Robot Movement Demo - Oct 9 @ 2019.gif')
sheet=Image.new('RGB',(1200,650),'#182127');draw=ImageDraw.Draw(sheet)
print({'frames':gif.n_frames,'size':gif.size,'duration_ms':gif.info.get('duration')})
for i in range(12):
 frame=round(i*(gif.n_frames-1)/11);gif.seek(frame)
 im=gif.convert('RGB');im.save(root/f'.review/ftc-frame-{frame}.jpg',quality=95)
 im.thumbnail((285,270));x=i%6*200;y=i//6*325
 im.thumbnail((195,280));sheet.paste(im,(x,y));draw.text((x+5,y+287),f'Frame {frame}',fill='white')
sheet.save(root/'.review/ftc-contact.jpg')
