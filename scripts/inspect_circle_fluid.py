from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as E
b=Path(r'C:/Users/kiden/OneDrive - University of Hartford/Documents/Hartford Assignments/.LEGACY CLASSES')
p=b/'Semester 6/Circ Invert project/Presentation/FinalcirclesSP25.pptx'
with ZipFile(p) as z:
 for n in sorted(z.namelist()):
  if n.startswith('ppt/slides/slide') and n.endswith('.xml'):
   print(n, ' '.join(E.fromstring(z.read(n)).itertext()))
