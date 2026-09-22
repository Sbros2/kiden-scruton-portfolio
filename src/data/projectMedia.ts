import piezo1 from '../assets/projects/piezo-study-1.png';
import piezo9 from '../assets/projects/piezo-study-9.png';
import piezo11 from '../assets/projects/piezo-study-11.png';
import piezo17 from '../assets/projects/piezo-study-17.png';
import piezo3 from '../assets/projects/piezo-study-3.png';
import piezo4 from '../assets/projects/piezo-study-4.png';
import piezo15 from '../assets/projects/piezo-study-15.png';
import piezo19 from '../assets/projects/piezo-study-19.png';
import piezo20 from '../assets/projects/piezo-study-20.png';
import ftc0 from '../assets/projects/ftc-0.jpg';
import rocksatElectrical from '../assets/projects/rocksat-electrical.jpg';
import rocksatWiring from '../assets/projects/rocksat-wiring.jpg';
import rocksatTeam from '../assets/projects/rocksat-team.jpg';
import wallopsRocksatTeam from '../assets/projects/wallops-rocksat-team.jpg';
import wallopsRocksatCanister from '../assets/projects/wallops-rocksat-canister.jpg';
import wallopsRocksatPayloadPlate from '../assets/projects/wallops-rocksat-payload-plate.jpg';
import wallopsRockonNasaBoard from '../assets/projects/wallops-rockon-nasa-board.jpg';
import ftc3 from '../assets/projects/ftc-3.jpg';
import ftc5 from '../assets/projects/ftc-5.jpg';
import arshFit from '../assets/projects/arsh-fit.png';
import arshDesign from '../assets/projects/arsh-design.png';
import arshDisplay from '../assets/projects/arsh-display.jpeg';
import arshSlider from '../assets/projects/arsh-slider.png';
import hsrComplete from '../assets/projects/hsr-complete.jpg';
import hsrChassis from '../assets/projects/hsr-chassis.jpg';
import hsrPrint from '../assets/projects/hsr-print.jpg';
import hsrEarly from '../assets/projects/hsr-early.jpeg';
import monorail from '../assets/projects/monorail-prototype.jpeg';
import monorailCad from '../assets/projects/monorail-cad.png';
import rocksat from '../assets/projects/rocksat-assembly.jpg';
import rocksatBoard from '../assets/projects/rocksat-board.jpg';
import rocksatTest from '../assets/projects/rocksat-test.jpg';
import shelby from '../assets/projects/shelby.jpeg';
import pcb from '../assets/projects/pcb.jpg';
import type { ImageMetadata } from 'astro';
import fluidChannel from '../assets/projects/fluid-channel-velocity.jpg';
import fluidProfiles from '../assets/projects/fluid-channel-profiles.jpg';
import fluidLow from '../assets/projects/fluid-velocity-low.jpg';
import fluidHigh from '../assets/projects/fluid-velocity-high.jpg';
import fluidPressure from '../assets/projects/fluid-pressure.jpg';
import fluidRevolved from '../assets/projects/fluid-revolved.jpg';
import fluidMesh from '../assets/projects/fluid-mesh.jpg';
import fanAssembly from '../assets/projects/fan-assembly.jpg';
import fanExploded from '../assets/projects/fan-exploded.jpg';
import fanDeformation from '../assets/projects/fan-deformation.jpg';
import fanMesh from '../assets/projects/fan-mesh.jpg';
import fanMoment from '../assets/projects/fan-moment.jpg';
import fanStress from '../assets/projects/fan-stress.jpg';
import aeroCylinder from '../assets/projects/aero-cylinder.jpg';
import aeroCylinderStream from '../assets/projects/aero-cylinder-streamlines.jpg';
import aeroAirfoil from '../assets/projects/aero-airfoil.jpg';
import aeroAirfoilStream from '../assets/projects/aero-airfoil-streamlines.jpg';
import crceAssembly from '../assets/projects/crce-assembly.png';
import crceTop from '../assets/projects/crce-top.png';
import aiActuator from '../assets/projects/ai-actuator.png';
import aiBaseline from '../assets/projects/ai-baseline.png';
import aiRevision1 from '../assets/projects/ai-revision1.png';
import aiRevision2 from '../assets/projects/ai-revision2.png';

export type ProjectImage = { image: ImageMetadata; alt: string; caption: string; fit?: 'contain' | 'cover'; position?: string; };
export const projectMedia: Record<string, { cover: ProjectImage; gallery: ProjectImage[] }> = {
 'retro-industrial-fan':{cover:{image:fanAssembly,alt:'SolidWorks rendering of the retro-industrial three-blade desk fan.',caption:'Fan CAD assembly from my final design report.',fit:'contain'},gallery:[
 {image:fanExploded,alt:'Exploded CAD view of fan blades, motor, housing, and stand.',caption:'Exploded assembly view for documenting how the parts fit together.',fit:'contain'},
 {image:fanMesh,alt:'ANSYS mesh on the fan support and housing.',caption:'Finite-element mesh from the structural study.',fit:'contain'},
 {image:fanMoment,alt:'ANSYS moment boundary condition showing a 20 lbf-in applied moment on the fan shaft face.',caption:'Load definition: a 20 lbf·in moment applied at the shaft face to investigate the structural load path.',fit:'contain'},
 {image:fanStress,alt:'ANSYS equivalent von Mises stress contour with a localized maximum at the shaft connection.',caption:'Equivalent stress at the shaft connection. The localized peak calls for checking mesh convergence, constraints, and contact assumptions before judging strength.',fit:'contain'},
 {image:fanDeformation,alt:'ANSYS total-deformation contour on the fan support assembly.',caption:'Total-deformation visualization for the modeled load case.',fit:'contain'}]},
 'aerodynamic-panel-methods':{cover:{image:fluidRevolved,alt:'COMSOL revolved visualization of velocity in the axisymmetric flow model.',caption:'COMSOL fluid-mechanics study: revolved velocity visualization.',fit:'contain'},gallery:[
 {image:fluidChannel,alt:'COMSOL velocity field in the channel-flow model.',caption:'Channel study: stationary laminar-flow velocity field.',fit:'contain'},
 {image:fluidProfiles,alt:'COMSOL velocity profiles sampled at multiple streamwise positions.',caption:'Channel study: comparing profiles at several streamwise locations.',fit:'contain'},
 {image:fluidMesh,alt:'Locally refined COMSOL mesh around the curved flow passage.',caption:'Axisymmetric study: local mesh and boundary-layer refinement.',fit:'contain'},
 {image:fluidLow,alt:'COMSOL velocity magnitude at 10 kPa inlet pressure.',caption:'Pressure sweep: velocity at 10 kPa inlet pressure. Read the individual color scale.',fit:'contain'},
 {image:fluidHigh,alt:'COMSOL velocity magnitude at 210 kPa inlet pressure.',caption:'Pressure sweep: velocity at 210 kPa inlet pressure. Color scales may differ between cases.',fit:'contain'},
 {image:fluidPressure,alt:'COMSOL pressure contours in the axisymmetric passage.',caption:'Pressure distribution from the second COMSOL report.',fit:'contain'},
 {image:aeroAirfoil,alt:'Numerical pressure contours around a NACA 0017 airfoil.',caption:'External flow: NACA 0017 pressure-contour visualization.',fit:'contain'},
 {image:aeroCylinder,alt:'Numerical pressure contours around a circular cylinder.',caption:'Study 1: pressure contours around a non-rotating cylinder.',fit:'contain'},
 {image:aeroCylinderStream,alt:'Potential-flow streamlines around a cylinder.',caption:'Study 1: cylinder streamlines.',fit:'contain'},
]},
 'crce-engine': {cover:{image:crceAssembly,alt:'Angled CAD view of the CRCE engine assembly showing the cylinders, central crank mechanism, and supports.',caption:'CRCE engine assembly in SolidWorks. CAD design view.',fit:'contain'},gallery:[
 {image:crceTop,alt:'Top CAD view of the CRCE engine assembly showing the arrangement of cylinders and connecting mechanisms.',caption:'Top view of the assembly, showing the component arrangement.',fit:'contain'},
 {image:crceAssembly,alt:'Isometric CAD view of the CRCE engine assembly.',caption:'Angled view of the cylinder arrangement and central mechanism.',fit:'contain'}]},
 'ai-assisted-motion-control': {cover:{image:aiActuator,alt:'Hydraulic actuator research rig with instrumentation and a LabVIEW computer.',caption:'Physical hydraulic test setup from the IMECE 2026 manuscript.',fit:'contain'},gallery:[
 {image:aiBaseline,alt:'Baseline controller five-run average position response against the target trajectory.',caption:'Profile 1: baseline physical response, averaged across five runs.',fit:'contain'},
 {image:aiRevision1,alt:'First AI-assisted controller revision five-run average position response.',caption:'Profile 2: improved physical tracking and reduced overshoot, with lower extension speed.',fit:'contain'},
 {image:aiRevision2,alt:'Second AI-assisted controller revision five-run average position response.',caption:'Profile 3: some speed recovered, with increased overshoot relative to Profile 2.',fit:'contain'}]},
 '2025-08-12-pcb-demo---copy-3': {
 cover: {image:ftc3,alt:'Team 10637 robot during its outdoor movement demonstration.',caption:'Frame from the 2019 movement demonstration, 5.7 seconds.',fit:'contain'},
 gallery:[{image:ftc0,alt:'FTC robot at the start of the outdoor demonstration.',caption:'Video still · 0.8 seconds.',fit:'contain'},{image:ftc3,alt:'FTC robot crossing the sunlit pavement.',caption:'Video still · 5.7 seconds.',fit:'contain'},{image:ftc5,alt:'FTC robot later in the movement demonstration.',caption:'Video still · 8.9 seconds.',fit:'contain'}]
 },
 arsh: {
  cover: { image: arshFit, alt: 'CAD view of the ARSH headset fitted to a head model, showing the display slider and side-mounted electronics.', caption: 'Headset fit study from the team’s final Expo poster.', position: '50% 42%' },
  gallery: [
   { image: arshDesign, alt: 'ARSH glasses design with camera and electronics mounted along the temples.', caption: 'The compact headset layout, from the team’s final poster.', fit: 'contain' },
   { image: arshDisplay, alt: 'The headset OLED displaying a scanned vibration-sensor warning.', caption: 'Working display: a QR scan returns demonstration vibration data.', fit: 'contain' },
   { image: arshSlider, alt: 'CAD model of the adjustable display slider.', caption: 'The slider gives the wearer control over the display distance.', fit: 'contain' },
  ],
 },
 'hazard-sensing-robot': {
  cover: { image: hsrComplete, alt: 'Completed Hazard Sensing Robot with yellow wheels, protective enclosure, and headlights illuminated.', caption: 'The completed HSR prototype with its lights on.', position: '50% 54%' },
  gallery: [
   { image: hsrEarly, alt: 'Early HSR proof of concept with exposed wiring and temporary construction.', caption: 'Early proof of concept: testing the arrangement before committing to a frame.' },
   { image: hsrPrint, alt: 'Printed HSR frame parts on an Ender printer bed.', caption: 'Printed frame iteration on the build plate.' },
   { image: hsrChassis, alt: 'HSR chassis with four wheels and protective frame, before final assembly.', caption: 'A later chassis revision, before final integration.' },
  ],
 },
 'brennan-gyro-monorail': {
  cover: { image: monorail, alt: 'Physical monorail prototype with two flywheels, a narrow wheelbase, and exposed control electronics.', caption: 'The physical gyroscopic stabilization prototype.', position: '50% 61%' },
  gallery: [{ image: monorailCad, alt: 'CAD assembly of the monorail chassis and its two flywheels.', caption: 'CAD assembly from the final project presentation.', fit: 'contain' }],
 },
 'rocksat-c': {
  cover: { image: wallopsRocksatPayloadPlate, alt: 'RockSat-C payload plate with Raspberry Pi, wiring, batteries, and sensors inside the cylindrical payload structure.', caption: 'RockSat-C payload plate integration during the Wallops Flight Facility trip.', position: '50% 52%' },
  gallery: [
   { image: wallopsRocksatPayloadPlate, alt: 'RockSat-C payload plate with Raspberry Pi, wiring, batteries, and sensors inside the cylindrical payload structure.', caption: 'Second Wallops trip: RockSat-C payload plate integration, wiring, and sensor layout during CT Space Grant-supported work.', fit: 'cover', position: '50% 47%' },
   { image: wallopsRocksatCanister, alt: 'RockSat-C payload canister with NASA and Hartford Hawks markings, showing internal wiring and electronics.', caption: 'Second Wallops trip: payload canister access during RockSat-C integration.', fit: 'contain' },
   { image: wallopsRocksatTeam, alt: 'University of Hartford students taking a group photo during the Wallops Flight Facility visit.', caption: 'Second Wallops Flight Facility trip with the RockSat-C team, supported by the Connecticut Space Grant Consortium.' },
   { image: wallopsRockonNasaBoard, alt: 'Kiden Scruton and Nick Krupa holding the RockOn board in front of a NASA meatball logo.', caption: 'First Wallops trip: Nick Krupa and I holding the RockOn board in front of the NASA meatball logo.', fit: 'contain' },
   { image: rocksatBoard, alt: 'Hand-wired prototype electronics board from RockSat-C testing.', caption: 'Prototype electronics during bench development.' },
   { image: rocksatTest, alt: 'RockSat-C assembly positioned alongside laboratory test equipment.', caption: 'Assembly and test setup from the project’s testing archive.' },
   { image: rocksatElectrical, alt: 'Wired electronics prototype with a multimeter and laptop on the bench.', caption: 'Electrical checks during subsystem development.', fit: 'contain' },
   { image: rocksatWiring, alt: 'Annotated photograph identifying separate boards and connections in the prototype.', caption: 'Annotated wiring reference from the testing archive.', fit: 'contain' },
   { image: rocksatTeam, alt: 'Payload electronics connected to a laptop during a team work session.', caption: 'Software and hardware integration with the team.' },
  ],
 },
 '26-2-10_shelby-corba': { cover: { image: shelby, alt: 'Shelby Cobra cutaway study showing internal mechanical components.', caption: 'Shelby Cobra cutaway study.', fit: 'contain' }, gallery: [] },
 '2025-08-12-pcb-demo': { cover: { image: piezo20, alt: 'Single-layer piezoelectric amplifier PCB design render showing component placement on the blue board.', caption: 'Single-layer PCB design render from the amplifier study. A simulated design concept for future RockSat-C research.', fit: 'contain' }, gallery: [
 {image:piezo1,alt:'PSpice AC sweep showing input, output, and an intermediate circuit node.',caption:'AC sweep from the original simulation study.',fit:'contain'},
 {image:piezo3,alt:'Extended PSpice frequency sweep showing attenuation at higher frequencies.',caption:'Extended sweep used to examine high-frequency roll-off.',fit:'contain'},
 {image:piezo4,alt:'Amplifier schematic detail identifying the test resistor and probe positions.',caption:'The load-comparison model uses a 10 kΩ placeholder resistor.',fit:'contain'},
 {image:piezo9,alt:'PSpice transient plot showing amplifier startup and the biased output waveform.',caption:'Small-signal transient case: the report specifies a 0.5 V, 200 Hz input.',fit:'contain'},
 {image:piezo11,alt:'FFT plot showing multiple harmonics in the high-amplitude simulated input case.',caption:'Overload FFT from the 10 V input case, documenting added harmonic content.',fit:'contain'},
 {image:piezo15,alt:'Two-channel amplifier schematic with separate inputs and shared supply.',caption:'Dual-channel circuit configuration for the transient and FFT study.',fit:'contain'},
 {image:piezo17,alt:'FFT plot of the two-channel simulated amplifier output.',caption:'Dual-channel FFT: the study uses 20 Hz and 200 Hz inputs.',fit:'contain'},
 {image:piezo19,alt:'AC sweep of the two-channel amplifier configuration.',caption:'Dual-channel AC sweep, checking that filtering and amplification remain present.',fit:'contain'},
 {image:pcb,alt:'Simulated piezoelectric amplifier schematic showing two amplifier circuits and voltage annotations.',caption:'Amplifier circuit simulation. Voltage annotations are simulated values.',fit:'contain'}
 ] },
};

