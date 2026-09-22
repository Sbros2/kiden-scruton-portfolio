from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]/'.review/plot-python'))
import shutil
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parents[1]
def write(p,s): (root/p).write_text(s,encoding='utf-8')
for i in [0,3,5]:
 shutil.copy2(root/f'.review/ftc-hd-{i}.jpg',root/f'src/assets/projects/ftc-{i}.jpg')
p=root/'src/data/projectMedia.ts'
s=p.read_text(encoding='utf-8')
s="import ftc0 from '../assets/projects/ftc-0.jpg';\nimport ftc3 from '../assets/projects/ftc-3.jpg';\nimport ftc5 from '../assets/projects/ftc-5.jpg';\n"+s
s=s.replace(" arsh: {", """ '2025-08-12-pcb-demo---copy-3': {
 cover: {image:ftc3,alt:'Team 10637 robot during its outdoor movement demonstration.',caption:'Frame from the 2019 movement demonstration, 5.7 seconds.',fit:'contain'},
 gallery:[{image:ftc0,alt:'FTC robot at the start of the outdoor demonstration.',caption:'Video still · 0.8 seconds.',fit:'contain'},{image:ftc3,alt:'FTC robot crossing the sunlit pavement.',caption:'Video still · 5.7 seconds.',fit:'contain'},{image:ftc5,alt:'FTC robot later in the movement demonstration.',caption:'Video still · 8.9 seconds.',fit:'contain'}]
 },
 arsh: {""")
p.write_text(s,encoding='utf-8')
p=root/'src/components/ProjectCard.astro'
s=p.read_text(encoding='utf-8').replace('const cover=projectMedia[entry.slug]?.cover;',"const cover=entry.slug==='2025-08-12-pcb-demo---copy-3'?undefined:projectMedia[entry.slug]?.cover;")
p.write_text(s,encoding='utf-8')
p=root/'src/layouts/ProjectLayout.astro'
s=p.read_text(encoding='utf-8').replace('const {entry}=Astro.props;','const {entry,showCover=true}=Astro.props;').replace('{media && <ProjectImage','{media && showCover && <ProjectImage')
p.write_text(s,encoding='utf-8')
write('src/pages/projects/2025-08-12-pcb-demo---copy-3.astro','''---
import {getEntry} from 'astro:content';
import ProjectLayout from '../../layouts/ProjectLayout.astro';
const entry=await getEntry('projects','2025-08-12-pcb-demo---copy-3');
---
<ProjectLayout entry={entry} showCover={false}>
 <figure slot="before-copy" class="demo-video"><video controls playsinline preload="metadata" aria-label="2019 Team 10637 robot movement demonstration"><source src="/assets/ftc-demo.mp4" type="video/mp4"/></video><figcaption>Team 10637 · 2019 movement demonstration · 13 seconds, no audio.</figcaption></figure>
 <h2>Building for competition</h2><p>My FTC work included a motorized lifting mechanism built with drawer sliders and sprockets, designed to let the robot lift itself for the endgame objective.</p>
 <h2>See the robot in motion</h2><p>The recording above shows the robot moving outdoors. The gallery below pulls out three full-resolution frames from that recording; it documents the movement demonstration, rather than a scored competition run or a verified lift test.</p>
</ProjectLayout>
''')
data=Path(r'C:\Users\kiden\Documents\.ACTUAL DOCS\Kiden\Code And Personal Proj\Piezo Circ\Vib_Analy_Data\IMUacc1.csv')
df=pd.read_csv(data).apply(pd.to_numeric)
t=(df.iloc[:,0].to_numpy()-df.iloc[0,0])/1000
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.facecolor':'#10191c','figure.facecolor':'#10191c','text.color':'#edf3f1','axes.labelcolor':'#a5b7b9','xtick.color':'#a5b7b9','ytick.color':'#a5b7b9','axes.edgecolor':'#3d555a','svg.fonttype':'none'})
fig,axs=plt.subplots(3,1,figsize=(12,7),sharex=True,layout='constrained')
for i,(ax,c) in enumerate(zip(axs,['#7ce6c4','#e4b56e','#8ebaf6'])):
 ax.plot(t,df.iloc[:,i+1],color=c,lw=.65)
 ax.set_ylabel(f'{"XYZ"[i]} (m/s²)');ax.grid(alpha=.12)
axs[0].set_title('Reference accelerometer record',loc='left',pad=16)
axs[-1].set_xlabel('Elapsed time from first sample (seconds)')
(root/'public/assets/results').mkdir(exist_ok=True)
fig.savefig(root/'public/assets/results/reference-acceleration.svg')
out=df.copy();out.columns=['timestamp_ms','acceleration_x_m_s2','acceleration_y_m_s2','acceleration_z_m_s2'];out.to_csv(root/'public/assets/results/reference-acceleration.csv',index=False)
rows=''.join(f'<tr><th scope="row">{axis}</th><td>{df.iloc[:,i+1].min():.2f}</td><td>{df.iloc[:,i+1].max():.2f}</td></tr>' for i,axis in enumerate('XYZ'))
write('src/pages/projects/rocksat-c.astro','''---
import {getEntry} from 'astro:content';
import ProjectLayout from '../../layouts/ProjectLayout.astro';
const entry=await getEntry('projects','rocksat-c');
---
<ProjectLayout entry={entry}>
 <h2>From vibration research to payload integration</h2><p>As a RockSat-C co-lead, I worked on the vibration subsystem: analyzing accelerometer records in Python, exploring piezoelectric energy harvesting, developing the transducer assembly, and coordinating payload work and budgets.</p>
 <p>The broader University of Hartford HAWKS mission investigated solar effects. My vibration work connected signal analysis with the design and integration of a physical experiment.</p>
 <h2>Mission outcome</h2><p>Professor Enrico Obst’s June 27, 2025 mission report confirms a successful launch, recovery, and data collection, and names Nicholas Krupa and me as the launch team. That establishes mission completion; it does not quantify the piezoelectric subsystem’s electrical output.</p>
 <p><a href="https://www.linkedin.com/pulse/rocksat-c-student-payload-success-enrico-obst-8ohwe">Read the mission success report ↗</a> · <a href="https://www.hartford.edu/news/press-releases/2025/03/ns-nasa-rocket.aspx">University mission overview ↗</a></p>
 <section slot="after-gallery" class="results-section">
  <div class="section-top"><div><p class="eyebrow">Analysis & results</p><h2>Understanding the vibration environment</h2></div></div>
  <div class="prose"><p>My January project write-up describes using earlier RockOn data to guide the RockSat design. The record below comes from that local vibration-analysis archive. It is <strong>reference data, not the 2025 RockSat-C flight results</strong>.</p></div>
  <dl class="project-facts"><div><dt>Samples</dt><dd>13,577 per axis</dd></div><div><dt>Record duration</dt><dd>496.239 seconds</dd></div><div><dt>Median sample interval</dt><dd>36 milliseconds</dd></div></dl>
  <figure class="result-chart"><a href="/assets/results/reference-acceleration.svg" target="_blank" rel="noopener"><img src="/assets/results/reference-acceleration.svg" width="1200" height="700" loading="lazy" alt="Three acceleration traces over 496 seconds. Activity varies across the record, with pronounced excursions near its end. Numerical ranges are given in the table below."/></a><figcaption>All recorded samples, plotted against their original timestamps. No smoothing or resampling. Units follow the source CSV headers; acceleration includes gravity.</figcaption></figure>
  <div class="result-details"><div><h3>Recorded acceleration range</h3><table><thead><tr><th>Axis</th><th>Minimum (m/s²)</th><th>Maximum (m/s²)</th></tr></thead><tbody>'''+rows+'''</tbody></table></div><div class="prose"><h3>What the record supports</h3><p>The changing acceleration provides input for investigating vibration and selecting a transducer arrangement. These extrema describe this record only; they are not a vibration qualification envelope or evidence of harvested power.</p><p>The timestamps are uneven. Frequency analysis needs to account for the native sampling rate; interpolating to a higher rate does not add measured bandwidth.</p><a href="/assets/results/reference-acceleration.csv" download>Download the plotted reference data (CSV) ↓</a></div></div>
  <div class="prose"><h3>2025 subsystem measurements</h3><p>The mission report confirms data collection. The accessible 2025 Flight Data folder contains no measurements, so flight-specific voltage, harvested energy, and subsystem performance are not reported here.</p></div>
 </section>
</ProjectLayout>
''')
write('src/pages/projects/brennan-gyro-monorail.astro','''---
import {getEntry} from 'astro:content';
import ProjectLayout from '../../layouts/ProjectLayout.astro';
import GyroSim from '../../components/GyroSim.jsx';
const entry=await getEntry('projects','brennan-gyro-monorail');
---
<ProjectLayout entry={entry}>
 <h2>Balancing a narrow vehicle</h2><p>A Brennan-inspired prototype explored using two counter-rotating flywheels and controlled actuation to resist tipping. I connected dynamic modeling and LabVIEW simulation with CAD, electronics, and a physical build.</p>
 <h2>Building and testing</h2><p>The hardware included a cart, flywheel assembly, motors, and a prototype motor controller using a MOSFET and drill battery. The build was semi-functional: excessive flywheel weight and inconsistent motor speeds limited its performance.</p>
 <h2>Lessons from the prototype</h2><p>The next iteration would use lighter flywheels and independent closed-loop speed control. The project showed how actuator limits and mechanical inertia can constrain an otherwise promising control model.</p>
 <section slot="after-gallery" class="section-block"><div class="section-top"><div><p class="eyebrow">Explore the model</p><h2>Stabilization simulator</h2></div></div><div class="prose"><p>This browser model explores an idealized roll response using proportional and derivative control. It illustrates parameter effects; it does not reproduce measured prototype performance or the full coupled flywheel dynamics.</p></div><GyroSim client:visible /></section>
</ProjectLayout>
''')
for name in ['about','resume','resources']:
 p=root/f'src/pages/{name}.astro';s=p.read_text(encoding='utf-8').replace('<h1 class="page-heading">','<header class="page-header"><h1>').replace('</p><article','</p></header><article').replace('</p><section','</p></header><section');p.write_text(s,encoding='utf-8')
p=root/'src/styles/site.css'
with p.open('a',encoding='utf-8') as f:f.write('''
.demo-video{margin:0 0 35px}.demo-video video{display:block;width:100%;max-height:650px;background:#000;border:1px solid var(--border);border-radius:12px}.demo-video figcaption,.result-chart figcaption{font-size:12px;color:var(--muted);margin-top:12px}.results-section{margin:65px 0}.result-chart{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:18px}.result-chart img{width:100%;height:auto}.result-details{display:grid;grid-template-columns:1fr 1fr;gap:40px;margin:35px 0}.result-details h3{margin-bottom:16px}table{border-collapse:collapse;width:100%;font-size:13px}th,td{text-align:left;padding:12px 9px;border-bottom:1px solid var(--border)}th{color:var(--muted);font-weight:500}.panel{max-width:800px}.results-section>.prose{max-width:850px}@media(max-width:700px){.result-details{grid-template-columns:1fr;gap:25px}.result-chart{padding:8px}.result-chart figcaption{padding:8px}table{font-size:11px}}
''')
p=root/'src/content/projects/rocksat-c.md';s=p.read_text(encoding='utf-8').replace('This overview covers development work. Flight results will be added alongside the corresponding test and mission records.','The mission completed launch, recovery, and data collection in June 2025. The project page distinguishes this confirmed mission outcome from earlier reference-data analysis.');p.write_text(s,encoding='utf-8')
write('public/favicon.svg','<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0b1113"/><text x="8" y="43" font-family="Arial,sans-serif" font-weight="700" font-size="33" fill="#7ce6c4">KS</text></svg>')
print('Updated project pages, original media, and reference-data results.')
