---
title: "AI-assisted motion control"
discipline: "Controls & AI research"
role: "Undergraduate researcher · paper co-author"
outcome: "Iterative controller study with physical validation"
order: 8
date: "2026-07-13"
summary: "Using actuator data, an empirical model, and iterative AI-assisted tuning to improve a hydraulic fuzzy controller."
tags: ["LabVIEW", "Python", "Fuzzy control", "Experimental analysis"]
---
## Making AI useful at the workbench
This research connected AI-assisted controller design to a real digital hydraulic linear actuator. The question was practical: could a model-informed revision improve the way the piston followed a target, and would the improvement survive physical testing?

I contributed to the research and co-authored **AI-Enhanced Motion Control for Digital Hydraulic Linear Actuators**, manuscript IMECE2026-193162. My project records include the controller-design workflow, analysis, and revisions explaining how the AI suggestions were implemented and evaluated.

## The iterative optimization loop
We started with an operator-designed fuzzy controller in LabVIEW. Position error drove two valve duty-cycle outputs. The AI received the original controller, an empirical actuator model, baseline simulation, five physical runs, and extracted performance metrics.

1. Measure the current controller’s tracking error, overshoot, speed, and valve usage.
2. Give those results and the actuator model to the AI to propose revised membership functions and rules.
3. Manually implement the proposed profile in LabVIEW.
4. Run the simulation and physical tests, then feed the results into the next revision.

This made the process recursive in the sense that each iteration used the previous results. The actuator still ran the LabVIEW controller; the AI acted as a design assistant between experiments.

## What the physical tests showed
The study compared three profiles, with five physical runs per profile and an approximately 125-second reference trajectory. Values below are the aggregate metrics reported in the final draft.

| Physical-test metric | Baseline | AI revision 1 | AI revision 2 |
| --- | --- | --- | --- |
| Cumulative absolute error (cm·s) | 515.814 | 411.781 | 412.644 |
| Mean run-level worst overshoot (%) | 55.994 | 43.225 | 46.066 |
| Final absolute error (cm) | 2.273 | 1.965 | 2.041 |
| Robust maximum extension velocity (cm/s) | 15.556 | 9.615 | 11.667 |

The first AI-assisted revision reduced cumulative error by **20.17%** and mean worst overshoot by **22.80%** relative to baseline. It also moved more slowly. The second revision recovered some extension speed, but overshoot and final error increased.

## The engineering judgment
The most useful result was understanding the tradeoff. A faster revision did not automatically make a better tracking controller. The empirical simulation also failed to reproduce the physical velocity and overshoot rankings, so hardware results remained the deciding evidence.

The test campaign used an unloaded actuator. Operating pressure and oil temperature were not recorded, and the reduced model omitted several hydraulic effects. These results describe the tested configuration and trajectory.

## The paper
The final draft lists Claudio Campana, Kiden Scruton, Kyle Burke, Shihab Sarwar, Asif Kingshuk, and Akin Tatoglu as authors. It is prepared for ASME’s International Mechanical Engineering Congress and Exposition (IMECE 2026). [Read the final draft](https://raw.githubusercontent.com/Sbros2/kiden-scruton-portfolio/main/public/documents/ai-motion-control-manuscript.pdf), the source for this page’s figures and reported results.
