from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import simpleSplit
from pypdf import PdfReader
import pypdfium2 as pdfium
out=Path('output/pdf');out.mkdir(parents=True,exist_ok=True)
dest=out/'kiden-portfolio-questionnaire.pdf'
c=canvas.Canvas(str(dest),pagesize=(612,792));c.setTitle('Kiden - Making the portfolio feel like you')
ink=HexColor('#172b30');teal=HexColor('#137568');muted=HexColor('#536970')
pages=[('The work you want to be known for',[
 ('open','1. Kiden, what made the monorail harder - and more rewarding - than HSR?','Describe a specific hardware problem, your decision, and what happened.'),
 ('open','2. Which monorail decisions were yours, and where did teammates lead?','Name a part, mechanism, wiring choice, or test. Credit people in your own words.'),
 ('open','3. If you had another month and a realistic budget, what would you change?','What would you build or test first, and what result would convince you it helped?'),
 ('closed','4. Which work would you most like to do next? Select up to two.',['Mechanical design','Hardware prototyping','Test / validation','Electronics','Aerospace systems','Still exploring']),
 ('closed','5. How should software appear in your story? Choose one.',['A tool for hardware','An equal interest','A separate interest']),
 ('closed','6. Which project should visitors explore first? Choose one.',['Brennan monorail','RockSat-C','ARSH','Another project']),
 ('closed','7. How should unfinished projects appear? Choose one.',['Alongside completed builds','In a separate experiments area','Only when there is a clear result'])
]),('The person behind the projects',[
 ('open','8. What should someone remember about you after closing the site?','Use words you would say to a friend. What does the current site get wrong?'),
 ('open','9. Tell me one moment from the shop or chapter that matters to you.','What happened with your family or friends, and why does it still stay with you?'),
 ('open','10. What do you build, notice, or enjoy when nobody is grading you?','Include an interest or story that does not need to prove a professional skill.'),
 ('closed','11. Who is the most important visitor right now? Choose one.',['Hardware hiring team','Research collaborator','Potential teammate','Friends / personal archive']),
 ('closed','12. Which voice feels most like you? Choose one.',['Direct and conversational','Technical and concise','Reflective and personal']),
 ('closed','13. What should lead the homepage visually? Choose one.',['Real prototype photo','Photo of me building','Team / launch photo','Keep the ranger avatar']),
 ('closed','14. How prominent should awards and leadership be? Choose one.',['Brief highlights with the work','A dedicated section','Mostly on the resume'])
])]
for pi,(title,qs) in enumerate(pages,1):
 c.setFillColor(teal);c.rect(40,748,32,4,fill=1,stroke=0)
 c.setFont('Helvetica-Bold',10);c.drawString(40,730,'KIDEN / PORTFOLIO QUESTIONS')
 c.setFillColor(ink);c.setFont('Helvetica-Bold',20);c.drawString(40,701,title)
 c.setFont('Helvetica',9);c.setFillColor(muted)
 c.drawString(40,681,'Answer naturally. Short notes are enough. Skip anything you do not want on the site.')
 c.drawString(40,667,'Your answers guide later edits; this worksheet is separate from the public website.')
 y=641
 for qi,(kind,title,detail) in enumerate(qs):
  c.setFillColor(ink);c.setFont('Helvetica-Bold',10)
  lines=simpleSplit(title,'Helvetica-Bold',10,532)
  for line in lines:c.drawString(40,y,line);y-=13
  key=f'p{pi}q{qi}'
  if kind=='open':
   c.setFillColor(muted);c.setFont('Helvetica',8.5);c.drawString(40,y,detail);y-=9
   c.acroForm.textfield(name=key,tooltip=title,x=40,y=y-54,width=532,height=54,fontSize=10,fontName='Helvetica',borderWidth=.5,borderColor=HexColor('#b9cac8'),fillColor=HexColor('#f6f9f8'),textColor=ink,fieldFlags='multiline',forceBorder=True)
   y-=71
  else:
   x=40;row=0
   for oi,opt in enumerate(detail):
    width=c.stringWidth(opt,'Helvetica',9)+30
    if x+width>573:x=40;y-=22
    c.acroForm.checkbox(name=key+str(oi),tooltip=opt,x=x,y=y-9,size=10,borderWidth=.7,borderColor=teal,fillColor=white,buttonStyle='check',forceBorder=True)
    c.setFont('Helvetica',9);c.setFillColor(ink);c.drawString(x+16,y-7,opt);x+=width
   y-=31
 c.setStrokeColor(HexColor('#d1ddda'));c.line(40,42,572,42)
 c.setFillColor(muted);c.setFont('Helvetica',8);c.drawString(40,27,'You can type into this PDF, print it, or reply in chat using the question numbers.')
 c.drawRightString(572,27,f'{pi} / 2');assert y>45,y;c.showPage()
c.save()
r=PdfReader(dest);assert len(r.pages)==2;assert len(r.get_fields())==36,len(r.get_fields())
pdf=pdfium.PdfDocument(str(dest));qa=Path('.review/questionnaire');qa.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(pdf):page.render(scale=1.4).to_pil().save(qa/f'page-{i+1}.png')
print(dest,'2 pages;',len(r.get_fields()),'fillable fields')
