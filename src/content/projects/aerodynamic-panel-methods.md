---
title: "Fluid simulations"
discipline: "Fluid mechanics & simulation"
role: "COMSOL studies & MATLAB flow analysis"
outcome: "Internal-flow and external-flow numerical studies"
order: 11
date: "2025-12-13"
summary: "COMSOL fluid-mechanics studies and MATLAB panel methods exploring velocity, pressure, mesh design, and flow around solid bodies."
tags: ["COMSOL", "MATLAB", "Fluid mechanics", "Numerical methods"]
---
## Studying flow from different directions
This collection brings together my COMSOL fluid-mechanics reports and MATLAB aerodynamic studies. The COMSOL models investigate internal laminar flow, while the panel-method work examines idealized external flow around a cylinder and airfoil.

## COMSOL: channel-flow study
My first report uses a stationary laminar-flow model with liquid water and a 1 cm/s inlet velocity. The geometry parameters include a 1.5 cm inlet length, 3 cm outlet length, 0.25 cm inlet radius, and 1 cm outlet width.

I used boundary selections, tetrahedral meshing, local refinement, and boundary layers to define the model, then examined velocity fields and profiles at several streamwise locations. The figures show the modeled flow and how it is sampled, rather than physical-test photographs.

## COMSOL: pressure-driven axisymmetric study
The second report uses an axisymmetric laminar-flow model and a stationary inlet-pressure sweep from 10 to 210 kPa in 40 kPa increments. The report includes velocity views at both endpoints, pressure contours, viscosity plots, and a revolved visualization of the solution.

The mesh uses triangular elements with local refinement and boundary layers. These figures document the simulation setup and predicted fields; selecting a fine mesh by itself does not establish mesh independence or physical validation.

## Turning a flow model into code
I used a source-panel method to approximate inviscid, incompressible flow. The solver divides a surface into panels and solves for source strengths using the no-penetration condition at panel control points.

## Study 1: a non-rotating cylinder
I compared pressure distributions for 8, 32, and 100 panels, plotted pressure contours and streamlines, and compared the numerical pressure distribution with the analytical cylinder solution.

The report records discrepancies that did not improve simply by adding panels. That made checking geometry, panel orientation, and error calculations part of the result, rather than treating a finer discretization as automatic validation.

## Study 2: NACA 0017
I applied the workflow to a symmetric airfoil at zero angle of attack, examining pressure coefficients, pressure contours, streamlines, and force coefficients over a range of panel counts. The archive includes XFOIL comparison attempts and output figures.

## Interpreting the results
These are numerical coursework investigations, not wind-tunnel measurements. The inviscid source-only model does not capture boundary-layer losses, separation, or realistic viscous drag. Discrepancies in pressure and force coefficients remain part of the solver-validation discussion.
