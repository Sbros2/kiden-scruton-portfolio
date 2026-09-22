---
title: "Circle inversion explorations"
discipline: "Mathematics & visualization"
role: "Computational geometry & animation"
outcome: "Python and MATLAB visual experiments"
order: 12
date: "2025-05-01"
summary: "Exploring repeated geometric inversions through code, point trajectories, and animated visualizations."
tags: ["Python", "MATLAB", "Geometry", "Visualization"]
thumbnail: "/assets/circle-inversions.gif"
---
## Making geometry visible
This project explores what happens when points are repeatedly inverted through circles. I used computational experiments and animations to make the transformations easier to inspect and explain.

## The transformation
For a circle centered at O with radius r, a point P maps to O + r²(P − O) / ‖P − O‖². The center itself is excluded because the denominator is zero. Points close to the center can map far away, making scale and plotting limits important.

## Repeated inversions
The two-circle Python demonstration alternates between two inversion circles, records the resulting trajectory, and fits a circle through its first three points. Other files explore four-circle sequences, randomized choices, and inversion of a sine curve.

## From geometric construction to code
Our Spring 2025 Special Topics in Mathematics presentation, credited to Gilad and Kiden, begins with the geometric construction and then develops computational examples. The progression includes single points, lines, functions, changing inversion circles, and repeated inversions.

For a single fixed inversion circle, applying the transformation twice returns the original point. Lines through the center remain on the same line; lines away from the center become circles through it. These relationships give useful checks on the plotted output.

## Why the inversion order matters
With more than two circles, selecting the next circle becomes part of the experiment. The presentation compares four approaches:

| Sequence | What it explores |
| --- | --- |
| Periodic | Repeat a fixed order such as A → B → C. |
| Randomized | Choose each next circle randomly; consecutive identical choices can undo one another. |
| Random chunks | Randomly order complete groups so each circle is used within a group. |
| Selective chunks | Also avoid matching the last circle of one group with the first of the next. |

The animations below compare fixed and randomized sequences and show how the resulting trajectories change. The presentation also explores overlapping-circle cases, four-circle patterns, and a possible extension to three dimensions.

## Original presentation
[Download the final Spring 2025 presentation](https://raw.githubusercontent.com/Sbros2/kiden-scruton-portfolio/main/public/documents/circle-inversions-final.pptx) for the full sequence of constructions, examples, and animations.

## What the visuals establish
The animations make patterns and sensitivity visible. A fitted curve or a finite sequence is an observation to investigate, rather than a proof of a general geometric result. The project combines that visual intuition with explicit transformation code.
