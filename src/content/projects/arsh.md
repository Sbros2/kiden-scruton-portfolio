---
discipline: "Wearable systems"
role: "Programming & procurement lead"
outcome: "HSB section winner, Spring 2024"
recognition: "HSB section winner"
order: 1
title: "ARSH wearable sensing headset"
date: "2024-04-26"
summary: "HSB-sponsored Expo section winner: a wearable QR-scanning interface for IoT demonstrations."
tags: ["Python", "Raspberry Pi", "Wearables", "Prototyping"]
---
## The challenge
Hartford Steam Boiler challenged student teams to create an interactive exhibit explaining how IoT sensors help prevent equipment damage and loss. The brief included proxy sensor data and a prototype demonstration.

## My contribution
I led programming and procurement, and shared hardware development with David Cole and Justin Niziolek. David led ergonomics and Justin led manufacturing.

## How it worked
A Raspberry Pi Zero 2 W and camera captured QR codes containing demonstration sensor information. Python decoded the information and presented it on a transparent OLED. The printed headset housed the electronics and battery, with an adjustable slider to accommodate viewing distance.

## Design iteration
We revised the frame and shifted the screen toward peripheral vision so that the wearer could glance at the information while keeping the main view clear. The design brought software, packaging, power, and viewing comfort together in one prototype.

## Recognition
Our team won the HSB-sponsored section of the Spring 2024 Expo. The university also lists the project as a sophomore honorable mention in its [official Expo recap](https://www.hartford.edu/news/press-releases/2024/05/ns-spring-ceta-expo-recap.aspx).

## Demonstrated scope
The prototype used QR-encoded demonstration data, consistent with the sponsor brief. Live network integration was a proposed extension.


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
