from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
def edit(file, old, new):
 p=root/file;s=p.read_text(encoding='utf-8');assert old in s,(file,old);p.write_text(s.replace(old,new),encoding='utf-8')
edit('src/pages/index.astro',"['arsh','hazard-sensing-robot','brennan-gyro-monorail','rocksat-c']","['brennan-gyro-monorail','rocksat-c','arsh','hazard-sensing-robot']")
edit('src/components/HeroIntro.astro','Aerospace / Embedded systems','Hardware / Mechanical design / Aerospace')
edit('src/components/HeroIntro.astro','Engineer. Hands-on builder.','I like building the hardware.')
edit('src/components/HeroIntro.astro','I build sensing robots, wearable interfaces, and experimental hardware—connecting software and electronics with the work of making things.','I’m most interested in mechanisms, electronics, and physical prototypes. My work ranges from a gyroscopic monorail to rocket payloads, using code and simulation to help the hardware work.')
edit('src/components/HeroIntro.astro','CREATIVITY MEETS ENGINEERING','MECHANISMS, ELECTRONICS & EXPERIMENTS')
edit('src/content/projects/brennan-gyro-monorail.md','role: "Modeling & prototyping"','role: "Mechanical design, electronics & prototyping"')
edit('src/content/projects/brennan-gyro-monorail.md','Brennan-inspired gyroscopic stabilization project combining dynamic modeling, PID control, LabVIEW simulation, and physical prototyping.','An ambitious hardware build combining counter-rotating flywheels, custom mounts, electronics, and control modeling. Actuator and flywheel limits shaped the outcome.')
edit('src/content/projects/brennan-gyro-monorail.md','outcome: "Physical prototype and interactive model"','outcome: "Semi-functional prototype; stabilization limited by actuation"')
# Keep the work archive curated without assigning equal weight to every study.
p=root/'src/pages/projects/index.astro';s=p.read_text();s=s.replace('---\n<BaseLayout',"const flagshipSlugs=['brennan-gyro-monorail','rocksat-c','arsh','hazard-sensing-robot'];\nconst flagship=flagshipSlugs.map(slug=>projects.find(p=>p.slug===slug)).filter(Boolean);\nconst studies=projects.filter(p=>!flagshipSlugs.includes(p.slug));\n---\n<BaseLayout")
s=s.replace('<p class="intro">The hardware, software, and design decisions behind my work.</p>','<p class="intro">Physical builds first, followed by the simulations, design studies, and personal experiments behind my interests.</p>')
s=s.replace('<section class="project-grid" aria-label="Engineering projects">{projects.map((entry,i)=><ProjectCard entry={entry} number={i+1}/>)}</section>','<section aria-labelledby="flagship-title"><div class="section-top"><h2 id="flagship-title">Selected hardware projects</h2></div><div class="project-grid">{flagship.map((entry,i)=><ProjectCard entry={entry} number={i+1}/>)}</div></section><section class="section-block" aria-labelledby="studies-title"><div class="section-top"><div><p class="eyebrow">Further exploration</p><h2 id="studies-title">Design studies & other projects</h2></div></div><div class="project-grid">{studies.map(entry=><ProjectCard entry={entry}/>)}</div></section>');p.write_text(s)
# Remove duplicated biography sections; retain confirmed facts and a compact community note.
p=root/'src/pages/about.astro';s=p.read_text(encoding='utf-8')
s=s.replace('My work brings together programming, electronics, mechanical design, and the hands-on process of building and testing.','My strongest interest is hardware: mechanical design, electronics, and the process of building and testing physical prototypes.')
start=s.index(' <div class="about-intro">');end=s.index(' <section class="section-block" aria-labelledby="experience-title">')
s=s[:start]+''' <div class="about-intro"><article class="prose"><h2>The hardware is what draws me in.</h2><p>The Brennan-inspired monorail is one of the projects I care most about. It was ambitious, and bringing together flywheels, motors, mounts, sensing, and control was harder than getting the HSR phone interface working.</p><p>That is the kind of work I want this portfolio to show: making physical parts fit and behave together, then finding out where the model and the hardware disagree. Code and simulation are part of that process.</p><p>The monorail did not reach reliable stabilization. It still represents a substantial part of my work, from mechanical design and parts selection to wiring and Arduino control.</p><a class="text-link" href="/projects/brennan-gyro-monorail/">Explore the monorail build →</a></article><aside class="about-focus"><p class="eyebrow">What I want to work on</p><h2>Mechanisms and working prototypes.</h2><p>I’m interested in work that puts mechanical design, electronics, fabrication, and testing in the same process, with aerospace as an important part of my background.</p><a class="text-link" href="/projects/">See the hardware projects →</a></aside></div>
'''+s[end:]
s=s.replace('<p>Those interests share something with my engineering work: curiosity about how things behave, and the patience to learn by doing.</p>','')
start=s.index(' <section class="section-block about-intro" aria-labelledby="internship-work">');end=s.index(' <div class="profile-cta">')
s=s[:start]+''' <section class="section-block prose" aria-labelledby="community-title"><p class="eyebrow">Around the workshop</p><h2 id="community-title">Teams and shared interests</h2><p>My university activities include AIAA and founding involvement in AURORA, the Advanced Undergraduate Rocketry Operations and Research Association. I also attended a 3D-printing conference in Boston in spring 2026.</p><p><a href="/resume/#leadership">Leadership, chapter founding, and the family business →</a></p></section>
'''+s[end:];p.write_text(s,encoding='utf-8')
# Keep the personal engine motivation ahead of file inventories.
p=root/'src/content/projects/crce-engine.md';s=p.read_text();start=s.index('## The assembly');end=s.index('## Design concept:');inventory=s[start:end];s=s[:start]+s[end:];s += '\n## CAD record\nThe downloadable assembly includes the block, pistons, connecting rods, crank, pins, and retaining parts. It is the current design record; dynamic analysis is the next step.\n';p.write_text(s)
# Gallery headings should reflect the work, not imply every study was built.
edit('src/layouts/ProjectLayout.astro',"{isSimulation?'Simulation figures & circuit design':'The build in detail'}","{isSimulation?'Simulation figures & circuit design':['aerodynamic-panel-methods','circle-inversions','ai-assisted-motion-control'].includes(entry.slug)?'Figures & analysis':entry.slug==='crce-engine'?'Design views':'The build in detail'}")
# Consolidate HSR into a short case study with one clear limitation paragraph.
p=root/'src/content/projects/hazard-sensing-robot.md';s=p.read_text();front=s[:s.index('## The challenge')];p.write_text(front+'''## The challenge
Build a compact robot that an operator could drive remotely while it recorded environmental conditions.

## What I built with the team
I reverse-engineered the app interface and adapted the robot to work with the Elegoo app on my phone for camera viewing and movement control. I also developed the XIAO sensor-logging program and an early proof of concept, and helped integrate the hardware. Movement software incorporated modified Elegoo code.

The Arduino Uno handled motion; a Seeeduino XIAO recorded DHT11 temperature/humidity and MQ-5 sensor outputs to microSD. A camera, lights, and printed enclosure completed the prototype.

## The decision that kept the demonstration workable
Live sensor-data transfer proved unreliable, so we kept camera viewing and remote driving on the phone and stored environmental readings onboard. Separating those functions gave us a workable demonstration without depending on an unreliable data link.

The report records frame prototypes 1–14. Wiring clearance, battery space, sensor placement, and print time drove the revisions; a frame took roughly five to six hours to print and the cage about three. Mechanical changes had a real cost in time.

## Outcome and next steps
The project tied for first place at the 2022 CETA Expo, and the university lists the team among its [winning projects](https://www.hartford.edu/unotes/2022/12/ceta-design-expo-features-student-inventions.aspx).

This was a student prototype. Gas readings were uncalibrated sensor outputs, waterproofing remained future work, and controller/shield reliability needed improvement. The original report and slides below preserve the team’s development record.
''')
