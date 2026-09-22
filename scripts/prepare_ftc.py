from pathlib import Path
import sys,subprocess,re
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'.review/python'))
import imageio_ffmpeg
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
source=Path(r'C:\Users\kiden\Documents\FTC Robot Movement.mp4')
info=subprocess.run([ffmpeg,'-hide_banner','-i',str(source)],capture_output=True,text=True).stderr
print(info[:4500])
match=re.search(r'Duration: (\d+):(\d+):([\d.]+)',info)
duration=int(match[1])*3600+int(match[2])*60+float(match[3])
frames=[]
for i in range(8):
 t=duration*(i+.5)/8
 dest=root/f'.review/ftc-hd-{i}.jpg'
 subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-y','-ss',str(t),'-i',str(source),'-frames:v','1','-q:v','2',str(dest)],check=True)
 frames.append((dest,t))
sheet=Image.new('RGB',(1200,760),'#182127');draw=ImageDraw.Draw(sheet)
for i,(path,t) in enumerate(frames):
 im=Image.open(path);im.thumbnail((285,325));x=i%4*300;y=i//4*380
 sheet.paste(im,(x+(300-im.width)//2,y));draw.text((x+8,y+340),f'{path.name} / {t:.1f}s',fill='white')
sheet.save(root/'.review/ftc-hd-contact.jpg')
subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-y','-i',str(source),'-vf','scale=trunc(iw/2)*2:trunc(ih/2)*2','-c:v','libx264','-crf','25','-preset','medium','-pix_fmt','yuv420p','-an','-movflags','+faststart',str(root/'public/assets/ftc-demo.mp4')],check=True)
print('Optimized muted video bytes:',(root/'public/assets/ftc-demo.mp4').stat().st_size)
