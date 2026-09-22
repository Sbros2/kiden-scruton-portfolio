from pathlib import Path
from pypdf import PdfReader
from zipfile import ZipFile
from xml.etree import ElementTree as ET
base=Path(r'C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments\RockSat-C')
for name in ['Rocksat-C 25.pdf','Rocksat-C 26.pdf','Rocksat-C 27.pdf']:
 print('\nFILE',name)
 for i,page in enumerate(PdfReader(base/name).pages):
  print('PAGE',i+1,page.extract_text())
for path in [base/'Write-Up Kiden Scruton 1_24.docx',Path(r'C:\Users\kiden\Downloads\STR Template RockSat C 2025.pptx')]:
 print('\nFILE',path.name)
 with ZipFile(path) as z:
  for name in z.namelist():
   if name=='word/document.xml' or (name.startswith('ppt/slides/slide') and name.endswith('.xml')):
    tree=ET.fromstring(z.read(name))
    print(' '.join(n.text or '' for n in tree.iter() if n.tag.endswith('}t')))
