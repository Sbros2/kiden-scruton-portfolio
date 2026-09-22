from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageDraw
base=Path(r'C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments\RockSat-C')
out=Path(__file__).resolve().parents[1]/'.review'
doc=pdfium.PdfDocument(base/'Rocksat-C 25.pdf')
sheet=Image.new('RGB',(1200,((len(doc)+3)//4)*240),'#182127')
draw=ImageDraw.Draw(sheet)
for i,page in enumerate(doc):
 im=page.render(scale=1.2).to_pil().convert('RGB')
 im.save(out/f'rocksat-page-{i+1}.png')
 im.thumbnail((285,210))
 x=i%4*300;y=i//4*240
 sheet.paste(im,(x,y));draw.text((x+4,y+215),f'Page {i+1}',fill='white')
sheet.save(out/'rocksat-pdf.jpg')
print('Pages:',len(doc))
