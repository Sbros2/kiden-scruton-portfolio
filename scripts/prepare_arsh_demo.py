from pathlib import Path
import sys, subprocess
from PIL import Image
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'.review/python'))
import imageio_ffmpeg
source=r'C:/Important Not Backed Up/Pictures/All IPhone Photos as of 6-1-26/PhotoSync/2024/04/05/IMG_8181.MOV'
target=root/'public/assets/arsh-display-demo.gif'
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-loglevel','error','-y','-i',source,'-filter_complex','fps=12,scale=360:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=none','-loop','0',str(target)],check=True)
with Image.open(target) as im: print(im.size, im.n_frames, target.stat().st_size)
