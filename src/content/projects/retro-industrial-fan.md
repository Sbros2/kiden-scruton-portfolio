---
title: "Retro-industrial desk fan"
discipline: "CAD & structural analysis"
role: "Design, assembly & ANSYS study"
outcome: "Fan assembly and structural load-case study"
order: 10
date: "2025-12-12"
summary: "A Fallout-inspired desk fan connecting parametric design, assembly planning, and moment-based structural analysis."
tags: ["SolidWorks", "ANSYS", "Structural analysis"]
---
## Designing something I would want on my desk
I designed a retro-industrial fan around a rugged, Fallout-inspired appearance. The engineering challenge was to keep that character while making the parts straightforward to manufacture and assemble.

## From parts to assembly
My SolidWorks design separates the stand, housing, blades, and motor. The exploded view documents how those parts come together. The archive also includes STL files prepared for printing the stand, housing, and blades.

## Structural study
I brought the assembly into ANSYS and investigated a moment-based loading case. The report describes ABS blades, steel motor/shaft components, bonded interfaces, and a fixed support. Its screenshots document the mesh, loading, stress, and deformation views.

The source describes the support location differently in different sections, so the load case needs that detail reconciled before numerical results are reused. The available figures are presented as study outputs, without claiming a verified safety factor or operating-speed limit.

## What I would refine next
The loading figure makes the structural question concrete: how does a **20 lbf·in applied moment** transfer through the shaft connection and support? The equivalent-stress figure identifies a localized maximum at that connection. I would use local mesh refinement and checks of the constraints and contacts to establish whether that peak represents meaningful component stress or a modeling artifact. The displayed maximum alone does not demonstrate an acceptable design.

The report focuses on shaft/hub load transfer, blade-root transitions, and stiffness. Improving airflow is a next design objective. Aerodynamic loading and transient effects were omitted from this structural study.
