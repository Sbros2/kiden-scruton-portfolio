from pathlib import Path
import sys, subprocess
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'.review/python'))
import imageio_ffmpeg
source=r'C:/Important Not Backed Up/Pictures/All IPhone Photos as of 6-1-26/PhotoSync/2024/04/05/IMG_8181.MOV'
ff=imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([ff,'-hide_banner','-i',source],stderr=subprocess.STDOUT)
for n,t in enumerate([0,2,4]):
 subprocess.run([ff,'-loglevel','error','-y','-ss',str(t),'-i',source,'-frames:v','1','-vf','scale=480:-1',str(root/f'.review/new-demo-{n}.jpg')],check=True)
