from pathlib import Path
import sys,subprocess
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'.review/python'))
import imageio_ffmpeg
subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(),'-hide_banner','-loglevel','error','-y','-i',str(root/'public/assets/ftc-demo.mp4'),'-vf','scale=1280:720','-c:v','libvpx-vp9','-crf','32','-b:v','0','-row-mt','1','-an',str(root/'public/assets/ftc-demo.webm')],check=True)
print('WebM bytes:',(root/'public/assets/ftc-demo.webm').stat().st_size)
