---
title: "deskthing"
author: "nimit vijayvargee"
description: "spotify car thing for non-car owners"
created_at: "2025-30-07"
---
# Total Time Spent: 5 Hours

# Schematic Design
Time Spent: 30 Minutes<br/> 
<br/>The schematic is a simple Pico W connected to a rotary encoder for the controls and a ST7735R screen to display. I hope to be able to diplay the album cover on the screen for aesthetic reasons. The rotary encoder has simple controls. Spinning normally fast-forwards or reverses a track, while double pressing it can play/pause. Pressing and then spinning the knob will be able to play the next or previous song. The Pi Pico W connects to the LCD via SPI, and has a knob. While it's size might be a lot, it is only used because of availability, as smaller wireless RP2040 boards are quite a lot more expensive.<br/> 
<img width="1087" height="850" alt="image" src="https://github.com/user-attachments/assets/daf569e1-1a05-42e7-9a88-d96029ac6475" />

# PCB Design
Time Spent: 30 Minutes<br/> 
The PCB is a basic 2 layer board that connects the screen and encoder to the pico, not much can be said. The size could be shrunk with a smaller board but that would increase the costs.<br/> 
I also spent some time setting up the 3D models so I could use the step file easily in the case. The ST7735 model is one I found online that matches my exact design. I also added headers to my Pico so it could be raised off the PCB (like how I intend to make it in the actual design).
<img width="880" height="699" alt="image" src="https://github.com/user-attachments/assets/8b51bf98-3ec1-4618-ae28-85f26e8a1e5a" /><br/> 


<img width="1237" height="432" alt="image" src="https://github.com/user-attachments/assets/b521f89b-2321-40d0-83d6-647f3e782ed5" />
<img width="889" height="401" alt="image" src="https://github.com/user-attachments/assets/6c8104bd-23ba-44a3-a684-a7efd1fe3126" />

# CAD Design
Time Spent: 1hr<br/> 
The first half of my time was spent adding all the step files to the PCB (especially the LCD). I then had to manually adjust the placements and offsets, which took some effort. I then took PCB Step into fusion and modelled a case around it. I also modelled a knob for it. After all the practice I got from highway, this was the fastest and coolest thing I have made using fusion!<br/> 
I started the CAD with importing a STEP file of the PCB into fusion, which I had previously added all the 3D models to. This way, most of the hard part was easily completed. I then made a sketch around the PCB, adding all the mounting holes too.
I then extruded the baseplate to accomodate the heatset inserts. I extruded the walls until they were on level with the LCD. Because of the way the PCB is set, the rotary encoder protruded a bit above the screen. I will use this to make a knob later on.
I also created an offset sketch on the extruded walls; where I put a plate for the front. It will slide around the screen and have a singular cutout for the knob (and also mounting holes). I also made a cutout for the Pico on the side so that I can power the device without having to worry about batteries.<br/> 
<img width="650" height="672" alt="image" src="https://github.com/user-attachments/assets/7a947070-3f23-4ab6-b1db-5213763d78ac" /><br/> 
<img width="985" height="527" alt="image" src="https://github.com/user-attachments/assets/6f79c059-b974-4de2-b09f-0a92f3067b4e" /><br/> 
<img width="1023" height="317" alt="image" src="https://github.com/user-attachments/assets/ffd8de4c-55a6-4c02-a1b1-30e5b478ef25" /><br/> 
Finally, I had to make the Knob. This is quite straightforward. First, I take the centre point of the encoder and create a circle around it. I also create an inner circle based on the dimesions of the rotary encoder, and a chord (for chorded encoders). If I don't use a chorded encoder, I can just melt the excess plastic off with a bad soldering iron tip lol. I then extrude everything except the core of the knob. While there are better ways to do this, I ended up creating another sketch, extruding the core back in and then sealing it off. The temporary sketch was what crossed my mind, although I could've just as easily used the Cut tool.
<img width="568" height="528" alt="image" src="https://github.com/user-attachments/assets/8364614b-ed05-4dc0-8d98-6ec4ad6adcb3" /><br/> 
<img width="259" height="263" alt="image" src="https://github.com/user-attachments/assets/4ced7249-a4ba-48dc-afad-1cf17f022f5f" /><br/> 
<img width="352" height="308" alt="image" src="https://github.com/user-attachments/assets/3ddd7483-b74e-4390-9220-7c403b4b69a5" /><br/> 
Finally, I rounded off the case a bit and added an emboss to the top. The fillets near the edges provide a radio style look (kind of ironic based on the project. I also curved the USB port; although idk how well the supports will handle this lol.
<img width="321" height="269" alt="image" src="https://github.com/user-attachments/assets/6347c8e6-0139-4d03-b5b7-70aa76625028" /><br/> 
<img width="836" height="622" alt="image" src="https://github.com/user-attachments/assets/69bde6a6-aa55-4709-b05a-b4973e56bf43" />
<img width="1061" height="639" alt="image" src="https://github.com/user-attachments/assets/9a6a0def-e9ea-4827-bbd5-8c83d30a4ed3" />

# Code
Time Spent: 2hr<br/> 
The code is written in circuitpython for a Pico W. It will initialize the display and connect to the Spotify Web SDK (Predefined credentials). It will then fetch the current playback status, and the album art to display on the screen. It takes all input from the encoder, parses and then passes it onto the API to perform actions as the user. The code was difficult to write as I had to combine both WiFi and Display features onto one device.
<br/>
I also ended up accidentally putting my WiFi details and API key (removed for now) into the git repo, so I had to do a clean wipe of that lol.
