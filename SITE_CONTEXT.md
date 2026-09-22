# Kiden Scruton portfolio context

This document supplies editorial context and draft content for the portfolio. It is an internal reference, not a public page. It combines Kiden's direct corrections, local project records, the resume, and university coverage. It does not establish that every resume statement is current.

## Purpose and audience

The site should help engineering employers, research collaborators, and graduate programs understand what Kiden has built, his individual contribution, how he solves problems, and what evidence supports the results. Emphasize working prototypes, software and hardware integration, design iteration, and honest lessons from testing.

The central story is an aerospace engineering background applied across embedded systems, sensing, robotics, fabrication, and experimental hardware. Leadership belongs alongside concrete technical decisions and deliverables.

## Draft homepage introduction

I build hardware and software systems that turn engineering ideas into working prototypes. My work spans environmental sensing robots, a wearable QR-scanning display, gyroscopic stabilization, and rocket payload development. I enjoy connecting embedded programming, electronics, fabrication, and testing to solve practical problems.

My background includes aerospace engineering studies at the University of Hartford, technical deployment work with Diagnostic Devices Inc., and helping students fabricate projects in the university Makerspace.

Editorial note: confirm current education and employment status before adding a graduation date, current job title, or internship availability. Do not use the resume's old future-tense launch statement as current status.

## Project priorities

1. ARSH: sponsor challenge, wearable interface, Python, hardware integration, award.
2. Hazard Sensing Robot: environmental data logging, remote operation, iterative enclosure development, award.
3. Brennan monorail: dynamic modeling, control simulation, prototype limitations, existing interactive page.
4. RockSat-C: payload development and signal analysis, with flight outcome to establish from later records.
5. FTC robotics: mechanism design and competition robot demonstration.
6. PCB, CAD, and fabrication examples: select projects with enough evidence to explain individual contributions.

## ARSH

### Identity and recognition

Use the short name ARSH and a descriptive subtitle such as "Wearable QR scanning and IoT demonstration headset." Source documents expand the acronym differently; avoid imposing a single official expansion until confirmed.

Kiden explicitly confirms that the team won the HSB-sponsored section of his year's Expo. The resume records first place at the Hartford Steam Boiler Expo 2024. The university's May 3, 2024 recap separately lists IOT Augmented Reality Glasses under sophomore honorable mentions, naming Kiden Scruton, David Cole, and Justin Niziolek. These describe different scopes of recognition. The public recap does not enumerate the HSB-specific results.

Suggested award wording: "Winner, HSB-sponsored section, Spring 2024 CETA Design Expo." Add the university-listed honorable mention separately. Do not imply overall first place across the entire Expo. The resume's March award label should not be treated as the event date; the university event announcement gives April 26, 2024.

### Sponsor brief

The local HSB and IoT Presentation Report describes an interactive exhibit challenge explaining how IoT sensors help prevent equipment damage, financial loss, and harm. HSB supplied proxy data and $100 per participating team. The task included a prototype and a five-minute pitch. Proxy data was part of the brief, so its use is appropriate to the demonstration. Sponsor funding is not proof of total build cost.

### Implementation and role

The final poster lists a Raspberry Pi Zero 2 W, Camera 2, a 1.51-inch transparent OLED, a 1000 mAh battery, power-management hardware, a button, a vibration motor, and a printed frame. It describes Python QR decoding and display of mock sensor information. The proposal lists Camera 3; use the final poster's Camera 2 provisionally and confirm against hardware photos if publishing detailed specifications.

The documented interaction is camera capture, QR decoding, interpretation of demonstration data, and display to the wearer. Avoid describing QR decoding as general-purpose object recognition or encryption/decryption. Live network integration was a proposed capability, not established by the original final poster.

The poster credits Kiden as Programmer and Procurement Lead, David as Co-Designer and Ergonomics Lead, and Justin as Co-Designer and Manufacturing Lead. The resume additionally describes Kiden as project lead, leading system/UI programming and sharing hardware development. Preserve team attribution.

Progress slides describe four frame revisions. The final design includes an adjustable slider for viewing distance and moves the screen toward peripheral vision to reduce obstruction of the main view.

### Draft project summary

I led programming and procurement for a three-person team building a wearable IoT demonstration headset for an HSB-sponsored design challenge. The prototype used a Raspberry Pi, camera, and transparent OLED to decode QR codes and present demonstration sensor information to the wearer. We iterated the printed frame and display position to improve viewing comfort. Our team won the HSB-sponsored section of the Spring 2024 Expo and received a sophomore honorable mention in the university's published results.

### ThirdEYE boundary

Kiden states that ThirdEYE is separate inspiration work. Do not merge its team, progress claims, internet connectivity work, or proposed commercial applications into ARSH. The Semester 6 ThirdEYE report is not evidence of a later ARSH product release or continuation.

## Hazard Sensing Robot

### Purpose and implementation

HSR is a compact environmental sensing robot intended to explore spaces where sending a person could be undesirable. The December 3, 2022 report describes an Arduino Uno for movement/control, a Seeeduino XIAO for sensing and microSD logging, a DHT11 temperature/humidity sensor, an MQ-5 gas sensor, camera functionality, lighting, and a printed protective enclosure.

The report explicitly attributes the XIAO program to Kiden. Slides identify his glued-together proof of concept and show frame versions V7, V8, and V13. The report references prototypes 1–14. The resume describes programming leadership and shared hardware development. Movement software incorporated modified Elegoo code; do not imply all underlying libraries and firmware were authored from scratch.

### Results and limitations

The team report states that the project tied for first at the 2022 Expo. The university's December 2022 article names HSR and its team among winning projects. It does not independently specify the tie or category rank.

Sensor data was recorded to microSD for later analysis. Wireless sensor-data transmission was abandoned following range/reliability problems. Distinguish that from camera streaming and remote control. Reports use inconsistent Bluetooth/Wi-Fi descriptions; inspect final firmware before making a detailed communications diagram.

Wiring and battery packaging required expanding the enclosure. Controller/shield problems caused interruptions. Waterproofing remained a goal rather than a demonstrated capability. The included gas code scales an analog reading; it does not establish gas-species concentrations, calibrated air quality, or safety certification. Avoid claims of proven suitability for firefighting, radiation, or extreme temperatures.

### Draft project summary

I helped develop a compact remote-operated robot that recorded temperature, humidity, and gas-sensor readings for later analysis. My work included sensor-logging software and early prototyping, alongside the team's repeated enclosure and hardware revisions. The project taught us how wiring space, component reliability, and communications limits shape an integrated robot. Our team tied for first place at the 2022 CETA Expo, according to our final project report.

## Brennan monorail

The existing page describes a Brennan-inspired gyroscopic stabilization prototype, LabVIEW modeling, PID control concepts, CAD, and a browser simulation. Its most useful story is the connection between modeled behavior and hardware constraints: flywheel weight, motor synchronization, and improvised motor control.

Treat the browser simulator as an illustrative model until the governing equation, signs, units, numerical behavior, and relationship to the physical prototype have been checked. Do not imply that simulation behavior proves physical stability. Supporting reports, CAD, test data, and prototype media still need to be connected to the page.

## RockSat-C

The resume describes Kiden as co-lead of a piezoelectric energy-harvesting payload project, including Fourier analysis of accelerometer data, transducer assembly design, prototyping, and team/budget coordination. It lists an October 2024 CT Space Grant award and a July 2025 planned launch. Confirm later design records, actual launch status, and results before publishing outcomes.

Candidate source folders are RockSat-C and RockOn Workshop 2024 Public. Keep the two programs distinct unless the files establish how work relates. Attribute student-team work accurately rather than implying NASA employment.

## Experience and skills

Resume-supported experience includes Diagnostic Devices Inc. deployment engineering, University of Hartford Makerspace work, founding leadership of Kappa Sigma, and co-founding Scruton Brothers Ice Cream. Use technical experience on the homepage and fuller leadership/business context on About.

Potential skills: Python, C++/Arduino, MATLAB, LabVIEW, signal analysis, PCB prototyping, soldering, microcontrollers, CAD, 3D printing, laser cutting, CNC, and hardware/software troubleshooting. Attach skills to project examples wherever possible. Confirm certification records before adding certification badges.

The newest named resume is KidenS Resume 2pg 2026.pdf, modified April 13, 2026. It still contains old future-tense plans and conflicting award date labels. The filename is not evidence that all content is current. HiveTech files exist but need project-specific review before any public description, especially because the folder contains an NDA.

## Site structure and next actions

- Home: concise introduction, strongest projects, clear resume/contact links.
- Projects: complete index with working destinations and accurate summaries.
- Project detail pages: problem, personal role, team, implementation, iteration, evidence, outcome, limitations.
- About: education, technical interests, experience, leadership, and selected skills.
- Resume: reviewed public resume with verified dates and appropriate contact information.
- Resources: genuine useful links; replace the placeholder YouTube URL.

The live review found 404s for Projects, Resources, About, Resume, FTC, Shelby Cobra, and PCB destinations. The FTC thumbnail appeared broken and the footer contained replacement characters. The monorail page loaded. Recheck current files before implementation; earlier source observations may no longer match the running site.

Before publishing project downloads, select final versions and remove grading comments, peer evaluations, personal records, private sharing links, and unrelated material. Preserve source files and copy only selected public assets. Do not copy this internal context document into public assets.

## Source map

Base academic folder: `C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments`

- HSR report: `.LEGACY CLASSES\Semester 1\ES 143\Expo Report\ES143_44470_T4_HazardSensingRobot_Final.docx`
- HSR slides: `.LEGACY CLASSES\Semester 1\ES 143\Expo Presentation\ES143_44470_ExpoPresentation_T4_95.pptx`
- ARSH final poster: `.LEGACY CLASSES\Semester 4\ENGR By Design\AR Smart headset A.R.S.H..pptx`
- ARSH sponsor context: `.LEGACY CLASSES\Semester 4\ENGR By Design\HSB and IoT Presentation Report.docx`
- ARSH development: `.LEGACY CLASSES\Semester 4\ENGR By Design\IoT Glasses.pptx` and `Progress Presentation2.pptx`
- Separate inspiration report: `.LEGACY CLASSES\Semester 6\Engr Lect\1Draft_ThirdEYE_ARSH_Report.pdf`
- Resume: `C:\Users\kiden\Documents\.ACTUAL DOCS\Kiden\Portfolio and Resume\KidenS Resume 2pg 2026.pdf`
- Spring 2024 university results: https://www.hartford.edu/news/press-releases/2024/05/ns-spring-ceta-expo-recap.aspx
- Spring 2024 event date: https://www.hartford.edu/unotes/2024/04/join-us-for-the-2024-spring-ceta-design-expo.aspx
- Fall 2022 university results: https://www.hartford.edu/unotes/2022/12/ceta-design-expo-features-student-inventions.aspx

Research context assembled September 2026. User corrections take precedence over earlier assistant assumptions; retain distinctions between user-confirmed facts, source-supported facts, and unresolved details.
