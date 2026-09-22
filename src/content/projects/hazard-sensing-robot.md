---
discipline: "Robotics & sensing"
role: "Programming & hardware integration"
outcome: "Tied first place, CETA Expo 2022"
recognition: "CETA Expo award"
order: 2
title: "Hazard Sensing Robot"
date: "2022-12-03"
summary: "A compact robot integrating remote operation, environmental sensing, and onboard data logging."
tags: ["Arduino", "Sensors", "C++", "3D printing"]
---
## The challenge
Build a compact robot that an operator could drive remotely while it recorded environmental conditions.

## What I built with the team
I reverse-engineered the app interface and adapted the robot to work with the Elegoo app on my phone for camera viewing and movement control. I also developed the XIAO sensor-logging program and an early proof of concept, and helped integrate the hardware. Movement software incorporated modified Elegoo code.

The Arduino Uno handled motion; a Seeeduino XIAO recorded DHT11 temperature/humidity and MQ-5 sensor outputs to microSD. A camera, lights, and printed enclosure completed the prototype.

## The decision that kept the demonstration workable
Live sensor-data transfer proved unreliable, so we kept camera viewing and remote driving on the phone and stored environmental readings onboard. Separating those functions gave us a workable demonstration without depending on an unreliable data link.

The report records frame prototypes 1–14. Wiring clearance, battery space, sensor placement, and print time drove the revisions; a frame took roughly five to six hours to print and the cage about three. Mechanical changes had a real cost in time.

## Outcome and next steps
The project tied for first place at the 2022 CETA Expo, and the university lists the team among its [winning projects](https://www.hartford.edu/unotes/2022/12/ceta-design-expo-features-student-inventions.aspx).

This was a student prototype. Gas readings were uncalibrated sensor outputs, waterproofing remained future work, and controller/shield reliability needed improvement. The original report and slides below preserve the team’s development record.
