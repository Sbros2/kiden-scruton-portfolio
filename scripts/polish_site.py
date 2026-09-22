from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
def write(path,text):
 p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')

write('src/layouts/BaseLayout.astro','''---
import '../styles/site.css';
import ImageViewer from '../components/ImageViewer.astro';
const {title='Kiden Scruton | Engineering Portfolio',description='Engineering projects by Kiden Scruton: embedded systems, sensing robots, wearable interfaces, and experimental hardware.'}=Astro.props;
const path=Astro.url.pathname;
const nav=[['Work','/projects/'],['About','/about/'],['Resources','/resources/'],['Resume','/resume/']];
---
<!doctype html>
<html lang="en">
 <head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/><meta name="description" content={description}/><meta name="theme-color" content="#0b1113"/><title>{title}</title><link rel="icon" type="image/svg+xml" href="/favicon.svg"/><link rel="preconnect" href="https://fonts.googleapis.com"/><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@500;600;700&display=swap" rel="stylesheet"/></head>
 <body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="wrap nav"><a class="brand" href="/" aria-label="Kiden Scruton home"><span class="brand-mark" aria-hidden="true">KS<span>.</span></span><span class="brand-name">KIDEN SCRUTON<small>ENGINEERING PORTFOLIO</small></span></a><nav aria-label="Main navigation">{nav.map(([label,url])=><a href={url} aria-current={path.startsWith(url)?'page':undefined}>{label}</a>)}</nav></div></header>
  <main id="main" class="wrap"><slot/></main>
  <footer class="site-footer"><div class="wrap"><div class="footer-top"><div><p class="eyebrow">Get in touch</p><h2>Let’s talk engineering.</h2></div><a class="contact-link" href="mailto:scrutonkiden@gmail.com">scrutonkiden@gmail.com <span aria-hidden="true">↗</span></a></div><div class="footer-bottom"><span>© {new Date().getFullYear()} Kiden Scruton</span><div><a href="/resume/">Resume</a><a href="https://www.linkedin.com/in/Kiden-Scruton/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="/resources/">Resources</a></div></div></div></footer>
  <ImageViewer/>
 </body>
</html>
''')
write('src/components/ProjectCard.astro','''---
import {Image} from 'astro:assets';
import {projectMedia} from '../data/projectMedia';
const {entry,number}=Astro.props;
const data=entry.data;
const cover=projectMedia[entry.slug]?.cover;
const widths=cover?[360,640,960].filter(w=>w<Math.min(cover.image.width,1200)).concat(Math.min(cover.image.width,1200)):[];
---
<article class="project-card">
 <a class="project-card-link" href={`/projects/${entry.slug}/`}>
  <div class="card-image" style={`--image-fit:${cover?.fit||'cover'};--image-position:${cover?.position||'center'}`}>
   {cover ? <Image src={cover.image} alt={cover.alt} widths={widths} sizes="(max-width: 700px) 92vw, (max-width: 1100px) 46vw, 560px" format="webp" quality={78} loading="lazy" /> : data.thumbnail && <img src={data.thumbnail} alt={data.title} loading="lazy" width="640" height="480" />}
   {data.recognition && <span class="card-recognition">{data.recognition}</span>}
  </div>
  <div class="card-copy"><div class="card-meta"><span>{data.discipline||'Engineering study'}</span>{number && <span>{String(number).padStart(2,'0')}</span>}</div><h3>{data.title}<span aria-hidden="true">↗</span></h3><p>{data.summary}</p><div class="card-bottom"><span>{data.role||'Project study'}</span><span>View project <span aria-hidden="true">→</span></span></div></div>
 </a>
</article>
''')
write('src/components/HeroIntro.astro','''---
import {Image} from 'astro:assets';
import avatar from '../assets/avatar.jpg';
---
<section class="hero">
 <div class="hero-copy"><p class="eyebrow">Aerospace / Embedded systems</p><h1>Kiden Scruton<span>.</span></h1><p class="hero-title">Engineer. Hands-on builder.</p><p class="hero-description">I build sensing robots, wearable interfaces, and experimental hardware—connecting software and electronics with the work of making things.</p><div class="hero-actions"><a class="button primary" href="#selected-work">Explore my work <span aria-hidden="true">↘</span></a><a class="button" href="/about/">About me <span aria-hidden="true">→</span></a></div><p class="hero-footnote">University of Hartford <span>/</span> Aerospace engineering background</p></div>
 <figure class="hero-portrait"><Image src={avatar} alt="Kiden’s illustrated western ranger avatar" widths={[320,480,700]} sizes="(max-width: 700px) 75vw, 350px" format="webp" quality={82} loading="eager" fetchpriority="high"/><figcaption><span class="portrait-rule"></span>CREATIVITY MEETS ENGINEERING</figcaption></figure>
</section>
<style>
 .hero{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.8fr);align-items:center;gap:70px;padding:60px 0 56px;border-bottom:1px solid var(--border)}.hero h1{font-size:clamp(44px,5.7vw,76px);letter-spacing:-3px;line-height:1.04;margin:20px 0 14px}.hero h1 span{color:var(--cyan)}.hero-title{font-size:clamp(18px,2.4vw,25px);letter-spacing:-.4px;color:#d6e4e0}.hero-description{font-size:15px;color:var(--muted);max-width:475px;margin-top:23px;line-height:1.8}.hero-actions{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}.hero-footnote{font-size:10px;color:var(--muted);margin-top:34px;letter-spacing:.25px}.hero-footnote span{margin:0 9px;color:var(--cyan)}.hero-portrait{max-width:350px;width:100%;justify-self:end;position:relative}.hero-portrait img{width:100%;height:345px;object-fit:cover;border-radius:12px;border:1px solid var(--border);object-position:50% 40%}.hero-portrait figcaption{display:flex;align-items:center;gap:10px;font-size:8px;letter-spacing:1.6px;color:var(--muted);margin-top:13px}.portrait-rule{width:22px;height:1px;background:var(--cyan)}
 @media(max-width:900px){.hero{gap:30px}.hero-portrait img{height:320px}.hero-footnote{max-width:300px}}
 @media(max-width:700px){.hero{grid-template-columns:1fr;gap:30px;padding:38px 0}.hero h1{font-size:50px;letter-spacing:-2px}.hero-title{font-size:22px}.hero-description{font-size:14px}.hero-footnote{margin-top:25px;max-width:none}.hero-portrait{max-width:none;justify-self:start}.hero-portrait img{height:230px;object-position:50% 35%}.hero-portrait figcaption{font-size:8px}.hero-actions{margin-top:22px}}
</style>
''')
write('src/pages/index.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
import HeroIntro from '../components/HeroIntro.astro';
import ProjectCard from '../components/ProjectCard.astro';
import {getCollection} from 'astro:content';
const entries=await getCollection('projects');
const projects=['arsh','hazard-sensing-robot','brennan-gyro-monorail','rocksat-c'].map(slug=>entries.find(p=>p.slug===slug)).filter(Boolean);
---
<BaseLayout>
 <HeroIntro/>
 <section id="selected-work" class="section-block"><div class="section-top"><div><p class="eyebrow">Selected work</p><h2>Built, tested, refined.</h2></div><a class="text-link" href="/projects/">All projects <span aria-hidden="true">↗</span></a></div><div class="project-grid">{projects.map((entry,i)=><ProjectCard entry={entry} number={i+1}/>)}</div></section>
 <section class="experience-strip"><p class="eyebrow">Beyond the projects</p><h2>Practical experience.<br/>A collaborative approach.</h2><div><p>From technical deployment at Diagnostic Devices Inc. to supporting students in the Makerspace, I enjoy helping people get hardware working.</p><a class="text-link" href="/about/">Experience & background <span aria-hidden="true">→</span></a></div></section>
</BaseLayout>
<style>.experience-strip{display:grid;grid-template-columns:1fr 1.6fr;gap:18px 70px;border-top:1px solid var(--border);padding-top:35px}.experience-strip>.eyebrow{grid-column:1/-1}.experience-strip h2{font-size:30px;letter-spacing:-1px;line-height:1.3}.experience-strip>div p{font-size:15px;line-height:1.8;color:var(--muted);margin-bottom:20px}@media(max-width:700px){.experience-strip{grid-template-columns:1fr;gap:20px}.experience-strip h2{font-size:27px}}</style>
''')
write('src/pages/projects/index.astro','''---
import BaseLayout from '../../layouts/BaseLayout.astro';
import ProjectCard from '../../components/ProjectCard.astro';
import {getCollection} from 'astro:content';
const projects=(await getCollection('projects')).sort((a,b)=>(a.data.order??99)-(b.data.order??99));
---
<BaseLayout title="Projects | Kiden Scruton"><header class="page-header"><p class="eyebrow">The project archive</p><h1>Engineering in practice.</h1><p class="intro">The hardware, software, and design decisions behind my work.</p></header><section class="project-grid" aria-label="Engineering projects">{projects.map((entry,i)=><ProjectCard entry={entry} number={i+1}/>)}</section></BaseLayout>
''')
write('src/layouts/ProjectLayout.astro','''---
import BaseLayout from './BaseLayout.astro';
import ProjectImage from '../components/ProjectImage.astro';
import {projectMedia} from '../data/projectMedia';
const {entry}=Astro.props;
const data=entry.data;
const media=projectMedia[entry.slug];
---
<BaseLayout title={`${data.title} | Kiden Scruton`} description={data.summary}>
 <header class="page-header"><a class="breadcrumb" href="/projects/">← All projects</a><p class="eyebrow">{data.discipline||'Project study'}</p><h1>{data.title}</h1><p class="intro">{data.summary}</p></header>
 <dl class="project-facts"><div><dt>My role</dt><dd>{data.role||'Project study'}</dd></div><div><dt>Focus</dt><dd>{data.tags?.slice(0,3).join(', ')}</dd></div><div><dt>Outcome</dt><dd>{data.outcome||'Design exploration'}</dd></div></dl>
 {media && <ProjectImage media={media.cover} hero class="project-hero"/>}
 <slot name="before-copy"/>
 <div class="project-body"><aside class="project-aside"><p class="eyebrow">In this project</p>{data.tags?.map(tag=><p>{tag}</p>)}</aside><article class="prose"><slot/></article></div>
 {media?.gallery.length>0 && <section aria-label="Project photographs and design images"><div class="section-top"><div><p class="eyebrow">A closer look</p><h2>The build in detail</h2></div><p>Select an image to explore it.</p></div><div class:list={['gallery-grid',{two:media.gallery.length<3}]}>{media.gallery.map(item=><ProjectImage media={item}/>)}</div></section>}
 <slot name="after-gallery"/>
 <div class="project-next"><a href="/projects/">← Explore more projects</a><a href="mailto:scrutonkiden@gmail.com">Ask me about this project ↗</a></div>
</BaseLayout>
''')
write('src/pages/projects/[...slug].astro','''---
import ProjectLayout from '../../layouts/ProjectLayout.astro';
import {getCollection} from 'astro:content';
export async function getStaticPaths(){return (await getCollection('projects')).filter(p=>!['brennan-gyro-monorail','rocksat-c','2025-08-12-pcb-demo---copy-3'].includes(p.slug)).map(entry=>({params:{slug:entry.slug},props:{entry}}));}
const {entry}=Astro.props;
const {Content}=await entry.render();
---
<ProjectLayout entry={entry}><Content/></ProjectLayout>
''')
f=root/'src/content/config.ts';s=f.read_text(encoding='utf-8');s=s.replace('title: z.string(),','title: z.string(),\n        discipline: z.string().optional(),\n        role: z.string().optional(),\n        outcome: z.string().optional(),\n        recognition: z.string().optional(),\n        order: z.number().optional(),',1);f.write_text(s,encoding='utf-8')
metadata={
 'arsh':('Wearable systems','Programming & procurement lead','HSB section winner, Spring 2024','HSB section winner',1),
 'hazard-sensing-robot':('Robotics & sensing','Programming & hardware integration','Tied first place, CETA Expo 2022','CETA Expo award',2),
 'brennan-gyro-monorail':('Controls & mechatronics','Modeling & prototyping','Physical prototype and interactive model','',3),
 'rocksat-c':('Aerospace & electronics','Co-lead / vibration subsystem','Launch, recovery & data collection','Mission completed · June 2025',4),
 '2025-08-12-pcb-demo - Copy (3)':('Competition robotics','Mechanism design & integration','Team 10637 robot demonstration','',5),
 '26-2-10_Shelby Corba':('CAD & visualization','Cutaway study','Mechanical visualization','',6),
 '2025-08-12-pcb-demo':('Electronics','Circuit design study','Electronics preview','',7),
}
for name,(discipline,role,outcome,recognition,order) in metadata.items():
 f=root/f'src/content/projects/{name}.md';s=f.read_text(encoding='utf-8');s=s.replace('---\n',f'---\ndiscipline: "{discipline}"\nrole: "{role}"\noutcome: "{outcome}"\nrecognition: "{recognition}"\norder: {order}\n',1);f.write_text(s,encoding='utf-8')
write('src/pages/404.astro','''---
import BaseLayout from '../layouts/BaseLayout.astro';
---
<BaseLayout title="Page not found | Kiden Scruton"><section class="not-found"><p class="eyebrow">404 / Page not found</p><h1>Let’s get you back.</h1><p>This address doesn’t lead to a project. Explore the archive or return to the homepage.</p><a class="button primary" href="/projects/">Explore projects →</a></section></BaseLayout>
''')
f=root/'.gitignore';f.write_text(f.read_text()+'\n# Local source-review intermediates\n.review/\n',encoding='utf-8')
print('Updated layouts, navigation, homepage, project templates, and metadata.')
