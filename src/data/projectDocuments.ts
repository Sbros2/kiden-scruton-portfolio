export type ProjectDocument = {title:string;href:string;format:string;description:string};
export const projectDocuments:Record<string,ProjectDocument[]>={
 'retro-industrial-fan':[{title:'Fan design & structural report',href:'/documents/fan-design-report.docx',format:'DOCX',description:'Original CAD coursework report with assembly views, the ANSYS setup, and structural study figures.'}],
 'aerodynamic-panel-methods':[{title:'COMSOL channel-flow report',href:'/documents/comsol-channel-report.docx',format:'DOCX',description:'Original first fluid-mechanics report: geometry, water properties, laminar-flow setup, mesh, and velocity profiles.'},{title:'COMSOL pressure-sweep report',href:'/documents/comsol-pressure-report.docx',format:'DOCX',description:'Final second report: axisymmetric model, pressure sweep, velocity, pressure, viscosity, and mesh figures.'},{title:'Cylinder & airfoil panel-method report',href:'/documents/aerodynamics-panel-study.docx',format:'DOCX',description:'Original numerical investigations, flow plots, solver discussion, and MATLAB code.'}],
 'circle-inversions':[{title:'Circle inversions — final presentation',href:'/documents/circle-inversions-final.pptx',format:'PPTX',description:'Spring 2025 presentation by Gilad and Kiden, including geometric constructions, repeated inversions, sequencing algorithms, and embedded animations.'},{title:'Two-circle inversion demonstration',href:'/documents/two-circle-inversion.py',format:'PY',description:'Original Python transformation, alternating-circle trajectory, fitted-circle calculation, and animation code.'}],
 'crce-engine':[
 {title:'CRCE SolidWorks assembly & parts',href:'/documents/crce-solidworks-assembly.zip',format:'ZIP',description:'Original engine assembly and six component files: block, piston, connecting rod, crank, connecting-rod pin, and pin cap. Requires compatible CAD software.'}
 ],
 'ai-assisted-motion-control':[
 {title:'AI-enhanced motion control — final draft',href:'/documents/ai-motion-control-manuscript.pdf',format:'PDF',description:'Final draft of IMECE2026-193162, with the actuator setup, iterative tuning procedure, physical results, simulation comparison, and author credits.'}
 ],
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

