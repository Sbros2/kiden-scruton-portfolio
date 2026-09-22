from pathlib import Path
from zipfile import ZipFile
import subprocess, sys
from PIL import Image

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / '.review/python'))
import imageio_ffmpeg
source = root / '.review/hsr-running.mov'
with ZipFile(root / 'public/documents/hsr-expo-presentation.pptx') as archive:
    source.write_bytes(archive.read('ppt/media/media1.mov'))
target = root / 'public/assets/hsr-running-demo.gif'
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-loglevel', 'error', '-y', '-i', str(source), '-filter_complex', 'fps=10,scale=270:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64:stats_mode=diff[p];[b][p]paletteuse=dither=none', '-loop', '0', str(target)], check=True)
with Image.open(target) as image:
    print({'size': image.size, 'frames': image.n_frames, 'bytes': target.stat().st_size})
    image.seek(image.n_frames // 2)
    image.convert('RGB').save(root / '.review/hsr-demo-middle.jpg')

