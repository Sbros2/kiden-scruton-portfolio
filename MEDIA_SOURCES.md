# Media and measurement provenance

## Expanded project documentation

The Hartford Assignments / RockSat-C / Piezo Circ shortcut was resolved read-only and points to Documents / .ACTUAL DOCS / Kiden / Code And Personal Proj / Piezo Circ. The source `Final Draft/Pspice Testing.docx` supplies the amplifier's documented simulation conditions and nine extracted figures (original image1, 3, 4, 9, 11, 15, 17, 19, 20). `Piezo Electric Harvester/Piezoelectric Energy Proposal.docx` is a proposal, not experimental validation. The ADC references in the PSpice report vary between sections, so the web page treats the 10 kΩ load and approximately 15 kHz cutoff as study assumptions. The PCB is a rendered design, not evidence of fabrication.

Ten source files were copied into public/documents: two piezo research documents, the ARSH final poster and sponsor-brief summary, HSR final report and presentation, monorail modeling report and final presentation, and the RockSat development write-up and four-channel ADC test sketch. Descriptions and downloads are maintained in src/data/projectDocuments.ts. Original files preserve attribution and historical wording; do not infer final hardware validation from broad claims in older coursework. Personal forms, waivers, receipts, and peer evaluations were excluded.

Monorail implementation detail was checked against `Gyroscopic Scooter 405.docx` and `ME 505 Modeling Report.docx`: Kiden's mechanical selection, five printed mounts/adapters, Arduino work, joint LabVIEW work with Wilondja Jerome, and Evan Wheeler's build contribution. The modeling report states that holding-torque limits prevented final hardware tests and contains inconsistent solver/model descriptions. The web page preserves this distinction.

HSR expanded architecture and print-time constraints follow the final report. ARSH exhibit requirements follow the sponsor-brief summary. RockSat acquisition details follow the actual development code: Piezo_ADC_Test reads A16/A17/A0/A1 despite its stale A0–A3 comment; the 10 ms delay is nominal, not a measured exact sampling frequency.

## Piezoelectric amplifier correction

The user clarified that the former “Precision PCB Demo” was fully simulated piezoelectric amplifier research for future RockSat-C work. Renamed the public title and corrected the summary, role, outcome, tags, image caption, and project body. The existing URL remains available. The schematic is simulation evidence, not a fabricated PCB or flight-tested amplifier; no gain, bandwidth, or hardware-validation claim is made.

## About and Resume update

HiveTech AI employment: user confirmed May 2026–current and prototyping/development work on September 13, 2026. Public role description: Prototyping & Development Intern. Supporting responsibilities are summarized from the July 10 Wi-Fi field report, August 4 network transport report, August 10 power test report, and local CAD assembly records. No raw employer reports, device identifiers, network details, or internal performance measurements were added to the site.

DDI, Makerspace, Kappa Sigma, and Scruton Brothers dates and responsibilities follow KidenS Resume 2pg 2026.pdf. Education is described as aerospace engineering studies without assuming current enrollment or a conferred degree. Certifications and old future-tense plans are omitted. Profile experience is maintained in src/data/experience.ts.

All selected imagery depicts original project material; no generated hardware imagery was used.

| Project | Source | Published selections |
|---|---|---|
| ARSH | Semester 4 / ENGR By Design / AR Smart headset A.R.S.H..pptx and Progress Presentation2.pptx | Fit study, headset CAD, OLED demonstration, display slider |
| HSR | Semester 1 / ES 143 / Expo Presentation / ES143_44470_ExpoPresentation_T4_95.pptx | Completed robot, early prototype, print, chassis |
| Monorail | Semester 6 / Mechatron / Project / gyro_scooter_project_Final.pptx | Original prototype photograph and CAD |
| RockSat-C | Hartford Assignments / RockSat-C / Testing | IMG_1333, 1309, 1331, 1299, 1300, 1329 |
| FTC | Documents / FTC Robot Movement.mp4 | Muted video transcodes; stills at approximately 0.8, 5.7, 8.9 seconds |

RockSat reference chart: Documents / .ACTUAL DOCS / Kiden / Code And Personal Proj / Piezo Circ / Vib_Analy_Data / IMUacc1.csv. Numeric rows and timestamps are preserved in the downloadable CSV; duplicate export headers are normalized. Plot elapsed time is (timestamp - first timestamp)/1000, and axes are plotted without smoothing or resampling. Acceleration units follow the original headers. The exact mission identity and sensor calibration of this short reference file have not been independently established. The January 2025 write-up describes using earlier RockOn data for design analysis. Do not re-label this as the 2025 RockSat flight record.

Confirmed 2025 outcome: Professor Enrico Obst's June 27, 2025 mission report, linked on the project page, states successful launch, recovery, and data collection and identifies Kiden on the launch team. It provides no numeric energy-harvesting results. The accessible 2025 Flight Data directory is empty; expense receipt PDFs were excluded.

FTC stills are frames from a movement demonstration, not separately captured photographs or proof of a completed lifting test. Original animated GIF is retained on its project card.
# HSR running demonstration

`public/assets/hsr-running-demo.gif` is derived from `ppt/media/media1.mov` in the original `ES143_44470_ExpoPresentation_T4_95.pptx` (also available as `public/documents/hsr-expo-presentation.pptx`). The footage shows the assembled robot driving with its lights on. Converted to a looping 10 fps GIF, 270 pixels wide, without altering the sequence. This documents movement, not calibrated hazard-sensing performance.

`public/assets/arsh-display-demo.gif`: converted from user-supplied IMG_8181.MOV (PhotoSync/2024/04/05), confirmed by user as ARSH. Full 3.34-second sequence, 12 fps, silent GIF. Original contains development-display text; caption makes no additional performance claims.

`public/assets/piezo-falstad-demo.gif`: 16 native PNG exports from Falstad running the unchanged Final Draft/Falstad Schematic/Piezo_ProtoCirc4.txt. Sampled frames played at 160 ms each; an illustrative preview, not a continuous real-time recording. Circuit source copied to public/documents/piezo-falstad-circuit.txt.

AI motion-control project: figures extracted from Tatoglu AMR/Fuzzy Piston/Report/IMECE2026_AI_Enhanced_Motion_Control_PaperFinalDraft.pdf. Table 3 supplies the physical performance metrics. Listed as a manuscript draft, not independently verified publication. Personal contribution details remain bounded by the author listing and Kiden-named report revisions.
CRCE engine: seven original SolidWorks files from Documents/.ACTUAL DOCS/Kiden/Code And Personal Proj/CRCE. The SVG card is an explicitly labeled component map, not a CAD render. Native assembly and parts provided together as ZIP. No engine performance or acronym expansion inferred.
HSR phone app: user confirmed reverse-engineering the app and using the Elegoo phone app for remote viewing and movement control, September 14, 2026. Kept separate from microSD environmental logging.


CRCE CAD views supplied by the user September 14, 2026: crce-assembly.png from Screenshot 2026-09-14 161054.png; crce-top.png from codex-clipboard-c05c7f3d-f83f-4068-96e5-6da47a59162d.png. Original screenshots preserved, including the selected edge in the angled view. Replaces the component-map thumbnail with actual CAD imagery.


Circle expansion: FinalcirclesSP25.pptx and six original figures/animations from Semester 6/Circ Invert project/Presentation. Figures retained without mathematical alterations.
Fluid simulations: original figures extracted from .Current_Semester 9/Kiden Scruton CS1 Report and Kiden_Scruton_Report_2_FINAL.docx. Transparent report images composited on white for readability. Both source reports included. Existing aerodynamic project URL retained for compatibility.

# Leadership and gallery follow-ups — September 14, 2026

- Kappa Sigma crest: official https://www.kappasigma.org/logos-icons/ asset, Primary-Crest-Only-175x300.png, transparent PNG.
- Scruton Brother's logo: imagegen background extraction from the original Grandopeningflyer/3.docx artwork in the personal Scruton Bros folder. Saved as public/assets/scruton-brothers-logo.png. A residual halo remains; cleanup retry hit the image tool usage limit. Prompt: Extract only the existing logo, preserve artwork and lettering, remove flyer text and background, transparent alpha.
- User corrected chapter charter date to January 2026, consistent with the national installation announcement of January 24, 2026. Founding presidency dates retained separately.
- Business history: user confirms family built and ran the shop, closed 2023. Opening story at https://itsthesway.com/scruton-brothers-ice-cream-opens-on-morganton/ supports family involvement, daily operations and personal allergy motivation. Social links supplied by user.
- Three additional original Circle Invert project/Presentation figures: Multipint_inv_3.png, line through circ center.png, Sinwave-Single-Inversion.png. Copied unchanged into public/assets/circle-multipoint.png, circle-center-line.png and circle-sine-points.png.
