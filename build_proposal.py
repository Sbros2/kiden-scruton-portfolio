from pathlib import Path
import re

root=Path(__file__).parent
for source in (root/'src').rglob('*'):
    if source.suffix in ['.astro','.jsx','.md','.ts','.css']:
        try: source.read_text(encoding='utf-8')
        except UnicodeDecodeError: source.write_text(source.read_bytes().decode('cp1252'),encoding='utf-8')
def write(p,s):
    f=root/p; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(s,encoding='utf-8')
layout=root/'src/layouts/BaseLayout.astro'
s=layout.read_text(encoding='utf-8').replace('=---','---',1)
s=re.sub(r'import AuroraFlow.*\n','',s)
s=s.replace('<style>','<style is:global>').replace('�','©',1).replace('�','·')
s=s.replace('</style>', '''
      .page-heading {font-family:Orbitron, sans-serif;color:#7eeed4;margin:40px 0 16px;}
      .intro {max-width:760px;color:var(--muted);line-height:1.7;margin-bottom:28px;}
      .project-grid {display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin:24px 0;}
      .prose {max-width:820px;line-height:1.8;padding:28px;margin:24px 0;}
      .prose a, .text-link {color:var(--cyan);}
      .prose h2 {color:#7eeed4;margin-top:28px;}
      .prose img {max-width:100%;border-radius:12px;}
      .eyebrow {color:var(--amber);text-transform:uppercase;letter-spacing:2px;font-size:12px;}
      @media(max-width:800px){.project-grid{grid-template-columns:repeat(2,minmax(0,1fr));}.nav{flex-wrap:wrap;gap:16px;}.menu{display:flex;flex-wrap:wrap;gap:15px}.menu a{margin-left:0;font-size:12px}}
      @media(max-width:560px){.project-grid,.home-grid,.links-under-left{grid-template-columns:1fr}.prose{padding:18px}}
      @media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
    </style>''')
layout.write_text(s,encoding='utf-8')
hero=root/'src/components/HeroIntro.astro'
s=hero.read_text(encoding='utf-8')
s=re.sub(r'  bio = ".*",','  bio = "I build hardware and software systems that turn engineering ideas into working prototypes. My work spans sensing robots, wearable interfaces, gyroscopic stabilization, and rocket payload development. I connect embedded programming, electronics, fabrication, and testing to solve practical problems.",',s)
s=s.replace('`${name} portrait`','`${name} illustrated western avatar`')
hero.write_text(s,encoding='utf-8')
write('src/pages/index.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
import HeroIntro from '../components/HeroIntro.astro';
import ProjectCard from '../components/ProjectCard.astro';
import {getCollection} from 'astro:content';
const entries=await getCollection('projects');
const featured=['arsh','hazard-sensing-robot','brennan-gyro-monorail','rocksat-c'];
const projects=featured.map(slug=>entries.find(p=>p.slug===slug)).filter(Boolean);
---
<BaseLayout title="Kiden Scruton | Engineering Portfolio">
 <HeroIntro />
 <h2 class="page-heading">Selected engineering projects</h2>
 <p class="intro">Explore the prototypes, the decisions behind them, and what testing taught us.</p>
 <section class="home-grid" style="display:grid;gap:20px;margin:24px 0">{projects.map(entry=><ProjectCard entry={entry}/>)}</section>
 <a class="text-link" href="/projects/">Explore all projects →</a>
 <section class="prose panel"><div class="eyebrow">Experience across disciplines</div><h2>From the workbench to the field</h2><p>My background includes technical deployment with Diagnostic Devices Inc., student fabrication support in the University of Hartford Makerspace, and leadership on the RockSat-C team.</p><a href="/about/">More about my background →</a></section>
</BaseLayout>
''')
def project(slug,title,summary,body,tags,thumbnail=None,date='2024-04-26'):
    import json
    fm=f'---\ntitle: {json.dumps(title)}\ndate: "{date}"\nsummary: {json.dumps(summary)}\ntags: {json.dumps(tags)}\n'
    if thumbnail: fm+=f'thumbnail: {json.dumps(thumbnail)}\n'
    write(f'src/content/projects/{slug}.md',fm+'---\n'+body+'\n')
project('arsh','ARSH wearable sensing headset','HSB-sponsored Expo section winner: a wearable QR-scanning interface for IoT demonstrations.', '''## The challenge
Hartford Steam Boiler challenged student teams to create an interactive exhibit explaining how IoT sensors help prevent equipment damage and loss. The brief included proxy sensor data and a prototype demonstration.

## My contribution
I led programming and procurement, and shared hardware development with David Cole and Justin Niziolek. David led ergonomics and Justin led manufacturing.

## How it worked
A Raspberry Pi Zero 2 W and camera captured QR codes containing demonstration sensor information. Python decoded the information and presented it on a transparent OLED. The printed headset housed the electronics and battery, with an adjustable slider to accommodate viewing distance.

## Design iteration
We revised the frame and shifted the screen toward peripheral vision so that the wearer could glance at the information while keeping the main view clear. The design brought software, packaging, power, and viewing comfort together in one prototype.

## Recognition
Our team won the HSB-sponsored section of the Spring 2024 Expo. The university also lists the project as a sophomore honorable mention in its [official Expo recap](https://www.hartford.edu/news/press-releases/2024/05/ns-spring-ceta-expo-recap.aspx).

## Demonstrated scope
The prototype used QR-encoded demonstration data, consistent with the sponsor brief. Live network integration was a proposed extension.
''',['Python','Raspberry Pi','Wearables','Prototyping'])
project('hazard-sensing-robot','Hazard Sensing Robot','A compact robot integrating remote operation, environmental sensing, and onboard data logging.', '''## The challenge
Build a compact robot to explore confined spaces and record environmental conditions while its operator remains elsewhere.

## My contribution
I developed the XIAO sensor-logging program and an early proof of concept, and helped integrate the hardware with the team. Movement software incorporated modified Elegoo code.

## System design
An Arduino Uno handled movement and control while a Seeeduino XIAO recorded DHT11 temperature and humidity readings and MQ-5 gas-sensor values to microSD. A camera, lights, and printed protective enclosure supported remote exploration.

## What testing taught us
We repeatedly revised the frame as wiring and battery space became clearer. Wireless sensor-data transfer proved unreliable, so the final workflow used onboard storage for later analysis. Controller and shield reliability also affected development.

## Outcome
Our final report records a tie for first place at the 2022 CETA Expo. The university names our team among the [winning projects](https://www.hartford.edu/unotes/2022/12/ceta-design-expo-features-student-inventions.aspx).

The device was a student prototype. Gas readings were sensor outputs rather than calibrated gas concentrations; waterproofing remained a future goal.
''',['Arduino','Sensors','C++','3D printing'],date='2022-12-03')
project('rocksat-c','RockSat-C payload development','Piezoelectric energy-harvesting research combining rocket vibration analysis and payload prototyping.', '''## Project concept
Our team explored harvesting energy from rocket vibration using piezoelectric transducers.

## My contribution
As co-lead, my work included payload development, analysis of accelerometer data using Fourier transforms, transducer assembly design, prototyping, and coordination of team tasks and budgets.

## Engineering focus
The project connected signal analysis with physical design: understanding vibration behavior informed how we approached the transducer assembly and its integration into a payload.

This overview covers development work. Flight results will be added alongside the corresponding test and mission records.
''',['Signal processing','Payloads','Prototyping'],date='2024-10-01')
for f in (root/'src/content/projects').glob('*.md'):
    s=f.read_text(encoding='utf-8')
    s=s.replace('thumbnail: "FTC Robot','thumbnail: "/assets/FTC Robot')
    if 'FTC Robotics' in s:
        s=s.replace('This is a placeholder body.','''## Team 10637
This demonstration shows the 2019 FTC robot. My work included a motorized lifting mechanism using drawer sliders and sprockets, designed to let the robot lift itself for the endgame objective.

![FTC robot movement demonstration](/assets/FTC%20Robot%20Movement%20Demo%20-%20Oct%209%20%40%202019.gif)''')
    elif 'Shelby Cobra Cutaway' in s:
        s=s.replace('This is a placeholder body.','## Cutaway study\nA visual study of the Shelby Cobra, exposing the arrangement of its internal components.\n\n![Shelby Cobra cutaway](/assets/Shelby-Cobra-Cut-Away-Upscaled.jpeg)')
    elif 'Precision PCB Demo' in s:
        s=s.replace('3D interactive PCB preview tuned to mimic EasyEDA look.','A PCB design preview from my electronics portfolio.').replace('This is a placeholder body.','## PCB design preview\nA visual entry from my electronics work.\n\n![PCB preview](/assets/pcb-thumb.jpg)')
    f.write_text(s,encoding='utf-8')
write('src/pages/projects/index.astro','''---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ProjectCard from '../../components/ProjectCard.astro';
import {getCollection} from 'astro:content';
const projects=(await getCollection('projects')).sort((a,b)=>b.data.date.localeCompare(a.data.date));
---
<BaseLayout title="Projects | Kiden Scruton"><h1 class="page-heading">Engineering projects</h1><p class="intro">Embedded systems, controls, robotics, and hands-on fabrication. Each project captures a different part of how I build and learn.</p><section class="project-grid">{projects.map(entry=><ProjectCard entry={entry}/>)}</section></BaseLayout>
''')
write('src/pages/projects/[...slug].astro','''---
import BaseLayout from '../../layouts/BaseLayout.astro';
import {getCollection} from 'astro:content';
export async function getStaticPaths(){return (await getCollection('projects')).filter(p=>p.slug!=='brennan-gyro-monorail').map(entry=>({params:{slug:entry.slug},props:{entry}}));}
const {entry}=Astro.props;
const {Content}=await entry.render();
---
<BaseLayout title={`${entry.data.title} | Kiden Scruton`}><h1 class="page-heading">{entry.data.title}</h1><p class="intro">{entry.data.summary}</p><div class="eyebrow">{entry.data.tags?.join(' / ')}</div><article class="prose panel"><Content/></article><a class="text-link" href="/projects/">← All projects</a></BaseLayout>
''')
write('src/pages/about.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="About | Kiden Scruton"><h1 class="page-heading">About me</h1><p class="intro">Engineering through experimentation, practical construction, and collaboration.</p><article class="prose panel"><h2>Technical background</h2><p>My background is in aerospace engineering at the University of Hartford. I work across embedded programming, electronics, CAD, and fabrication, with an interest in connecting analysis to physical prototypes.</p><h2>Experience</h2><p>At Diagnostic Devices Inc., I worked on technical deployment and troubleshooting for a cardiovascular detection device. In the university Makerspace, I supported fabrication, equipment maintenance, and student training.</p><h2>Leadership</h2><p>I have served as a RockSat-C co-lead and founding president of the University of Hartford Kappa Sigma chapter. Before university, I co-founded Scruton Brothers Ice Cream, an allergy-friendly business.</p><h2>Tools I use</h2><p>Python, C++ and Arduino, MATLAB, LabVIEW, CAD, PCB prototyping, soldering, 3D printing, laser cutting, and CNC fabrication.</p><a href="/resume/">View my experience summary →</a></article></BaseLayout>
''')
write('src/pages/resume.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Resume | Kiden Scruton"><h1 class="page-heading">Experience & qualifications</h1><p class="intro">A concise overview of my engineering work, project leadership, and practical skills.</p><article class="prose panel"><h2>Education</h2><p>Aerospace engineering studies, University of Hartford.</p><h2>Engineering experience</h2><ul><li>Diagnostic Devices Inc. — R&amp;D deployment engineering and technical troubleshooting.</li><li>University of Hartford Makerspace — fabrication support, equipment maintenance, and student training.</li><li>RockSat-C — team co-lead, payload development, and vibration analysis.</li></ul><h2>Selected recognition</h2><ul><li>ARSH — HSB-sponsored Expo section winner, Spring 2024; university-listed sophomore honorable mention.</li><li>Hazard Sensing Robot — tied first place, CETA Expo 2022, as recorded in the team report.</li></ul><h2>Technical skills</h2><p>Embedded programming, signal analysis, CAD, electronics integration, prototyping, and fabrication.</p><h2>Contact</h2><p><a href="mailto:scrutonkiden@gmail.com">scrutonkiden@gmail.com</a> · <a href="https://www.linkedin.com/in/Kiden-Scruton/">LinkedIn</a></p></article></BaseLayout>
''')
write('src/pages/resources.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
import ResourceCard from '../components/ResourceCard.astro';
import {getCollection} from 'astro:content';
const resources=(await getCollection('resources')).filter(r=>!r.data.href.includes('xxxxx'));
---
<BaseLayout title="Resources | Kiden Scruton"><h1 class="page-heading">Resources & interests</h1><p class="intro">A small collection of links connected to building, systems, and creative problem-solving.</p><section class="project-grid">{resources.map(entry=><ResourceCard entry={entry}/>)}</section></BaseLayout>
''')
f=root/'src/content/resources/2025-08-12-opus-magnum.md'; f.write_text(f.read_text().replace('/assets/opus.jpg','/assets/assetsopus.jpg'),encoding='utf-8')
f=root/'src/pages/projects/brennan-gyro-monorail.astro'; s=f.read_text(); s=s.replace('(mgh + 2 * I_s *','(-mgh + 2 * I_s *'); s=s.replace('Browser recreation','Illustrative browser recreation'); f.write_text(s,encoding='utf-8')
f=root/'src/components/GyroSim.jsx'; s=f.read_text(); s=s.replace('onChange(parsed);','onChange(Math.min(max, Math.max(min, parsed)));'); s=s.replace('gridTemplateColumns: "320px 1fr"','gridTemplateColumns: "repeat(auto-fit, minmax(min(100%, 320px), 1fr))"'); f.write_text(s,encoding='utf-8')
f=root/'src/components/bg/ParallaxGrid.jsx'; s=f.read_text().replace('const c = ref.current, ctx = c.getContext("2d");','const c = ref.current, ctx = c.getContext("2d");\n        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;'); f.write_text(s,encoding='utf-8')
write('README.md','''# Proposed engineering portfolio

Independent source copy of the original site, with expanded project pages and navigation fixes. Original files remain in the parent directory.

Run `npm ci`, then `npm run dev -- --port 4322`. Build with `npm run build`.

The resume route is a curated HTML summary. The older PDF has not been published because its dates and future plans need updating. No private academic documents were copied into public assets. The simulation remains illustrative, not physically validated.
''')
