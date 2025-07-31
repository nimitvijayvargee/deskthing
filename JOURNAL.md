---
title: "deskthing"
author: "nimit vijayvargee"
description: "spotify car thing for non-car owners"
created_at: "2025-30-07"
---

# Schematic Design
Time Spent: 30 Minutes \
  The schematic is a simple Pico W connected to a rotary encoder for the controls and a ST7735R screen to display. I hope to be able to diplay the album cover on the screen for aesthetic reasons. The rotary encoder has simple controls. Spinning normally fast-forwards or reverses a track, while double pressing it can play/pause. Pressing and then spinning the knob will be able to play the next or previous song. The Pi Pico W connects to the LCD via SPI, and has a knob. While it's size might be a lot, it is only used because of availability, as smaller wireless RP2040 boards are quite a lot more expensive. \
<img width="1087" height="850" alt="image" src="https://github.com/user-attachments/assets/daf569e1-1a05-42e7-9a88-d96029ac6475" />

# PCB Design
Time Spent: 30 Minutes \
The PCB is a basic 2 layer board that connects the screen and encoder to the pico, not much can be said. The size could be shrunk with a smaller board but that would increase the costs. \
<img width="1237" height="432" alt="image" src="https://github.com/user-attachments/assets/b521f89b-2321-40d0-83d6-647f3e782ed5" />
<img width="889" height="401" alt="image" src="https://github.com/user-attachments/assets/6c8104bd-23ba-44a3-a684-a7efd1fe3126" />

# CAD Design
Time Spent: 1hr \
The first half of my time was spent adding all the step files to the PCB (especially the LCD). I then had to manually adjust the placements and offsets, which took some effort. I then took PCB Step into fusion and modelled a case around it. I also modelled a knob for it. After all the practice I got from highway, this was the fastest and coolest thing I have made using fusion! \
<img width="717" height="632" alt="image" src="https://github.com/user-attachments/assets/35c01b8f-fe03-4e03-8fb9-6ee6c57b6411" />
<img width="1061" height="639" alt="image" src="https://github.com/user-attachments/assets/9a6a0def-e9ea-4827-bbd5-8c83d30a4ed3" />

# Code
Time Spent: 2hr \
The code is written in circuitpython for a Pico W. It will initialize the display and connect to the Spotify Web SDK (Predefined credentials). It will then fetch the current playback status, and the album art to display on the screen. It takes all input from the encoder, parses and then passes it onto the API to perform actions as the user. The code was difficult to write as I had to combine both WiFi and Display features onto one device.
\
I also ended up accidentally putting my WiFi details and API key (removed for now) into the git repo, so I had to do a clean wipe of that lol.
