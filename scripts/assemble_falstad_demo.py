from pathlib import Path
from PIL import Image
import shutil
root=Path(__file__).resolve().parents[1]
paths=[Path(r'C:/Users/kiden/Downloads')/f'piezo-falstad-frame-{i:02d}.png' for i in range(1,17)]
frames=[Image.open(p).convert('RGB') for p in paths]
size=frames[0].size
assert all(f.size==size for f in frames)
assert len({f.tobytes() for f in frames})>1
frames[0].save(root/'public/assets/piezo-falstad-demo.gif',save_all=True,append_images=frames[1:],duration=160,loop=0,optimize=True)
source=Path(r'C:/Users/kiden/Documents/.ACTUAL DOCS/Kiden/Code And Personal Proj/Piezo Circ/Final Draft/Falstad Schematic/Piezo_ProtoCirc4.txt')
shutil.copy2(source,root/'public/documents/piezo-falstad-circuit.txt')
print('Animated Falstad preview:',size,len(frames))
