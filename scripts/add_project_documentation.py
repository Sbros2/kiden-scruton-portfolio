from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
a=Path(r'C:\Users\kiden\OneDrive - University of Hartford\Documents\Hartford Assignments')
p=Path(r'C:\Users\kiden\Documents\.ACTUAL DOCS\Kiden\Code And Personal Proj\Piezo Circ')
out=root/'public/documents';out.mkdir(exist_ok=True)
sources={
 'piezo-pspice-study.docx':p/'Final Draft/Pspice Testing.docx',
 'piezo-energy-proposal.docx':p/'Piezo Electric Harvester/Piezoelectric Energy Proposal.docx',
 'hsr-final-report.docx':a/'.LEGACY CLASSES/Semester 1/ES 143/Expo Report/ES143_44470_T4_HazardSensingRobot_Final.docx',
 'hsr-expo-presentation.pptx':a/'.LEGACY CLASSES/Semester 1/ES 143/Expo Presentation/ES143_44470_ExpoPresentation_T4_95.pptx',
 'arsh-final-poster.pptx':a/'.LEGACY CLASSES/Semester 4/ENGR By Design/AR Smart headset A.R.S.H..pptx',
 'arsh-sponsor-brief.docx':a/'.LEGACY CLASSES/Semester 4/ENGR By Design/HSB and IoT Presentation Report.docx',
 'monorail-modeling-report.docx':a/'.LEGACY CLASSES/Semester 6/Mechatron/Project/ME 505 Modeling Report.docx',
 'monorail-final-presentation.pptx':a/'.LEGACY CLASSES/Semester 6/Mechatron/Project/gyro_scooter_project_Final.pptx',
 'rocksat-development-writeup.docx':a/'RockSat-C/Write-Up Kiden Scruton 1_24.docx',
 'rocksat-piezo-adc-test.ino':a/'RockSat-C/Code/Piezo_ADC_Test/Piezo_ADC_Test.ino',
}
for name,src in sources.items():shutil.copy2(src,out/name)
for i in [1,3,4,15,19,20]:shutil.copy2(root/f'.review/documents/piezo-testing-image{i}.png',root/f'src/assets/projects/piezo-study-{i}.png')
def write(path,text):(root/path).write_text(text,encoding='utf-8')
write('src/data/projectDocuments.ts','''export type ProjectDocument = {title:string;href:string;format:string;description:string};
export const projectDocuments:Record<string,ProjectDocument[]>={
 '2025-08-12-pcb-demo':[
  {title:'PSpice simulation study',href:'/documents/piezo-pspice-study.docx',format:'DOCX',description:'Original AC sweeps, transient and FFT studies, load comparison, dual-channel design, and PCB layout rendering. Historical research notes; the amplifier work remained simulated.'},
  {title:'Piezoelectric energy proposal',href:'/documents/piezo-energy-proposal.docx',format:'DOCX',description:'Early research objectives covering transducer selection, mechanical coupling, AC-to-DC conversion, and measurement. Proposed work, not measured energy-harvesting results.'}
 ],
 'arsh':[
  {title:'Final Expo poster',href:'/documents/arsh-final-poster.pptx',format:'PPTX',description:'Team design overview, headset packaging, demonstration workflow, and contribution credits.'},
  {title:'HSB challenge brief',href:'/documents/arsh-sponsor-brief.docx',format:'DOCX',description:'Kiden’s summary of the sponsor challenge, proxy-data requirement, exhibit objective, and prototype constraints.'}
 ],
 'hazard-sensing-robot':[
  {title:'Final team report',href:'/documents/hsr-final-report.docx',format:'DOCX',description:'Design constraints, hardware architecture, iterations, demo observations, and code appendix. Original coursework; gas readings were not calibrated concentrations.'},
  {title:'Expo presentation',href:'/documents/hsr-expo-presentation.pptx',format:'PPTX',description:'The team’s build progression, prototype photographs, sensor integration, and presentation material.'}
 ],
 'brennan-gyro-monorail':[
  {title:'Modeling report',href:'/documents/monorail-modeling-report.docx',format:'DOCX',description:'Original LabVIEW model, parameter set, plots, and Arduino appendix. A working academic report; full hardware stabilization tests were not completed.'},
  {title:'Final project presentation',href:'/documents/monorail-final-presentation.pptx',format:'PPTX',description:'Mechanical concept, hardware, CAD, prototype, and project conclusions.'}
 ],
 'rocksat-c':[
  {title:'Vibration subsystem development notes',href:'/documents/rocksat-development-writeup.docx',format:'DOCX',description:'January development write-up connecting prior RockOn data analysis, piezoelectric research, and payload integration. Includes draft passages and planned work.'},
  {title:'Four-channel ADC test sketch',href:'/documents/rocksat-piezo-adc-test.ino',format:'INO',description:'Original development sketch: 12-bit readings from A16, A17, A0, and A1, with serial output and a 10 ms delay. Not identified as flight firmware.'}
 ],
 '2025-08-12-pcb-demo---copy-3':[
  {title:'2019 robot movement demonstration',href:'/assets/ftc-demo.mp4',format:'MP4',description:'The available motion record for Team 10637. This recording documents movement; it does not establish competition scoring or a completed lifting test.'}
 ]
};
''')
file=root/'src/data/projectMedia.ts';text=file.read_text(encoding='utf-8')
text='\n'.join(f"import piezo{i} from '../assets/projects/piezo-study-{i}.png';" for i in [1,3,4,15,19,20])+'\n'+text
text=text.replace("caption: 'Amplifier circuit simulation. Voltage annotations are simulated values; no fabricated PCB is shown.', fit: 'contain' }, gallery: []", """caption: 'Amplifier circuit simulation. Voltage annotations are simulated values; no fabricated PCB is shown.', fit: 'contain' }, gallery: [
 {image:piezo1,alt:'PSpice AC sweep showing input, output, and an intermediate circuit node.',caption:'AC sweep from the original simulation study.',fit:'contain'},
 {image:piezo3,alt:'Extended PSpice frequency sweep showing attenuation at higher frequencies.',caption:'Extended sweep used to examine high-frequency roll-off.',fit:'contain'},
 {image:piezo4,alt:'Amplifier schematic detail identifying the test resistor and probe positions.',caption:'The load-comparison model uses a 10 kΩ placeholder resistor.',fit:'contain'},
 {image:piezo15,alt:'Two-channel amplifier schematic with separate inputs and shared supply.',caption:'Dual-channel circuit configuration for the transient and FFT study.',fit:'contain'},
 {image:piezo19,alt:'AC sweep of the two-channel amplifier configuration.',caption:'Dual-channel AC sweep, checking that filtering and amplification remain present.',fit:'contain'},
 {image:piezo20,alt:'Rendered PCB layout derived from the simulated amplifier design.',caption:'PCB design rendering from the report; this is not a photograph of a fabricated board.',fit:'contain'}
 ]""")
file.write_text(text,encoding='utf-8')
file=root/'src/content/projects/2025-08-12-pcb-demo.md';front=file.read_text(encoding='utf-8').split('---',2)[1]
file.write_text('---'+front+'---\n'+'''## What I was investigating
I researched an amplifier and signal-conditioning circuit for piezoelectric measurements in future RockSat-C work. The aim was to prepare the alternating sensor signal for digitization by combining input limiting, DC bias, amplification, and filtering. The PSpice study examined these functions individually and then in a dual-channel arrangement.

This page covers the simulated amplifier study. The broader energy-harvesting proposal explores mechanical coupling, rectification, and storage as future research objectives; those objectives are not results of the amplifier simulation.

## Signal path and design choices
The design used an LMC662 operational amplifier. Its input and feedback networks were intended to preserve useful variation in the piezoelectric signal while shifting the operating level into a single-supply measurement range.

| Circuit function | Purpose in the study |
| --- | --- |
| Input limiting | Investigate how larger input excursions are constrained in the circuit model. |
| DC bias | Shift the alternating waveform to an operating level suitable for the modeled single-supply stage. |
| Amplification | Increase the amplitude of smaller signals before digitization. |
| High-pass behavior | Reduce the contribution of DC and very slow drift. |
| Low-pass behavior | Attenuate high-frequency content before the intended ADC interface. |

## Simulation program
The report combines frequency-domain and time-domain investigations. The conditions below come from the original study; they are simulated inputs, not flight measurements.

| Study | Conditions documented | Finding or question |
| --- | --- | --- |
| AC sweep | Initial sweep and an extended sweep to 200 kHz | Examined gain and roll-off, with a stated low-pass design target around 15 kHz. |
| Output loading | With and without a 10 kΩ placeholder load | The report describes similar modeled behavior in the two configurations. |
| Small-signal transient and FFT | 0.5 V, 200 Hz input over a four-second record | Examined startup, amplification, DC offset, and the frequency component. |
| Higher-amplitude input | 4 V input case | The report notes clipping near a supply rail and added harmonic content. |
| Overload exploration | 10 V input case | Harmonics at multiples of the 200 Hz input highlighted the limits of the modeled stage. |
| Dual-channel operation | Inputs described as 3 V at 200 Hz and 2 V at 20 Hz | Checked whether both input frequencies remained distinguishable with a shared supply and ground. |

## What the simulations showed
The study supported continuing development of the biased amplifier and filter arrangement. It also exposed an important limitation: larger inputs could clip and introduce harmonics. Recovering the main frequency in an FFT does not mean that the waveform is undistorted.

The load comparison tested a simplified resistor model. It does not establish compatibility with the dynamic input behavior of a real ADC, and the dual-channel results do not establish measured crosstalk performance.

## Design questions still open
The working report names different ADC devices in different sections. Its 10 kΩ load and approximately 15 kHz filter target should therefore be read as study assumptions, not a finalized acquisition specification. Selecting the actual ADC and sampling rate is necessary before judging the anti-aliasing requirements.

A physical follow-up would need to characterize the piezoelectric source, verify gain and frequency response, measure clipping and noise, and test the selected ADC interface. Those are proposed next steps. This project remains a fully simulated research study, including the PCB layout rendering shown below.

## Relationship to RockSat-C
This work informs a future research direction and is separate from the documented outcome of the 2025 payload mission. The [RockSat-C page](/projects/rocksat-c/) covers payload development, its available reference data, and the confirmed mission milestones.
''',encoding='utf-8')
file=root/'src/content/projects/arsh.md'
with file.open('a',encoding='utf-8') as f:f.write('''
## From sponsor brief to prototype
The sponsor brief called for an interactive exhibit explaining how IoT information could help prevent equipment damage and loss. It supplied proxy data and required a short concept presentation plus a prototype. That made a clear, repeatable demonstration more important than implementing a complete live sensor network.

Our headset presented that information close to the wearer’s field of view. A QR code supplied the demonstration data, the Raspberry Pi decoded it, and the OLED displayed the result. The housing and adjustable slider had to support both the electronics and a usable viewing position.

## System responsibilities
| Part of the system | Role |
| --- | --- |
| Camera and Raspberry Pi | Capture and decode QR-encoded demonstration information. |
| Python display workflow | Turn decoded data into the information shown to the wearer. |
| OLED and slider | Present the result while allowing adjustment of viewing distance. |
| Printed frame and battery packaging | Bring the optical, mechanical, and electrical pieces into a wearable prototype. |

The final poster below preserves the team’s contribution credits and design visuals. The sponsor brief explains the demonstration requirements that shaped those decisions.
''')
file=root/'src/content/projects/hazard-sensing-robot.md'
with file.open('a',encoding='utf-8') as f:f.write('''
## Architecture and data flow
The project separated motion control from environmental logging. The Arduino Uno handled the robot-control program, based on modified Elegoo kit code. The Seeeduino XIAO ran my logging program and recorded sensor outputs for later review.

| Subsystem | Function |
| --- | --- |
| Arduino Uno and motor hardware | Remote movement and tank-style steering. |
| Seeeduino XIAO | Independent environmental-data logging. |
| DHT11 and MQ-5 | Temperature/humidity readings and gas-sensor output. |
| microSD storage | Retain readings for post-run inspection and plotting. |
| Camera, lights, and enclosure | Support visibility and protect the integrated components. |

## Design constraints and iteration
The team report records frame prototypes 1–14. Sensor placement, wiring clearance, battery space, and print time drove repeated changes. The report estimates five to six hours for a frame print and about three hours for the cage, making each mechanical revision a meaningful scheduling decision.

The intended live sensor-data link was dropped after unreliable range and communication behavior. Local storage gave us a workable demonstration path. The report also records controller and shield problems, making component checks part of the integration process.

## Reading the original documentation
The report and slides capture the team’s development process and Expo demonstration. Some original language describes intended hazardous-environment applications; the prototype was not a qualified safety instrument. The MQ-5 output was not a calibrated measurement of individual gas concentrations, and waterproofing remained future work.
''')
print('Added source downloads, six amplifier figures, and expanded project narratives.')
