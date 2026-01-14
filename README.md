# ConsoleCapstone-MM-JC
Michael Monrroy's and Julius Conception's Capstone Project
!
Design process: 
Initial problem: 
The problem is that game consoles run out of battery too soon and screen glare makes usage of the console difficult outdoors. We’d use solar energy to power our console when there’s a light source similar to a battery. The console would be able to be powered by a rechargeable battery as well so at night the console would switch energy sources.

But our main focus switched to creating an interface that can select and play different games that is controlled by a joystick, buttons, and is displayed on a screen


Usage of Ms Hester's Arduino kit was used to build a foundational understanding of how LCD's and inputs work with Arduino

<img width="412" height="416" alt="Screenshot 2026-01-14 11 26 12 AM" src="https://github.com/user-attachments/assets/1e6a0283-b505-4748-9a9f-8bedbd9a0418" />


<img width="403" height="249" alt="Screenshot 2026-01-14 11 29 50 AM" src="https://github.com/user-attachments/assets/773575c5-90f7-41ba-86e7-166e794558e8" />

Disatisfied with the size of the display, I purchased a 3.5" display that would sit on top of the Raspberry Pi, taking up pins that would make it difficult to directly connect buttons to the Pi. 

<img width="150" height="131" alt="Screenshot 2026-01-14 11 31 53 AM" src="https://github.com/user-attachments/assets/4a980f9f-f10c-46d3-82ee-4a51d1e3bc1c" />


For our inputs, we used Ms Hester's Arduino and used serial communication with the Raspberry Pi to allow for the readings of our inputs.

Skills demonstrated:
Usage of Python: learnt to adapt to Python syntax, learning about tabbing, try syntax, if statements, utilized Python libraries to access features of the Raspberry Pi such as keyboard inputs and time
Usage of Arduino: learnt to use a physical Arduino board to connect buttons and joysticks to the Raspberry pi through serial communication with Python code
Organization: Physical layout of the Arduino board changed through the course of the project as my partner and I simplified the usage of our wires
Adaptability: Worked on majority of project through a minature 3.5" display, forcing me to get used to coding on an uncomfortable setup


Reflection:
This project taught me to utilize the principles of the engineering design process to create a product that would solve our problem, even if our outcome was different from what we believed it would be. It was important not to go straight into hardware and code, as I had no experience using a Linux-based OS or Python and Arduino. Utilizing Ms Hester's kits gave me a foundation of how to work with hardware alongside software. I found that this project enhanced my problem solving skills as I was limited to a restrictive 32 bit os which forced me to find alternatives to normal programs that I would've used, for example to run my java game I had to search for an old enough program that would run on an older system to run my code and that was Visual Studio Code. In addition, I was restricted to the 3.5" display which forced me to adapt to a difficult testing environment. I didn't want to bug my project by reinstalling drivers to be able to use a monitor through HDMI so I stook with the display.

Initial Layout:
<img width="612" height="792" alt="initial layout" src="https://github.com/user-attachments/assets/d8ba7447-3555-40c2-978a-30b2a3a4723f" />
Final Layout:
<img width="621" height="720" alt="final design" src="https://github.com/user-attachments/assets/3fbf5cee-6735-4fa3-97a3-840573aac3a4" />

Work done to ensure the display would connect

Raspberry pi imager used to switch to 32 bit os (bookworm legacy) 
done to solve connection errors for display 
some of the drivers were dated and worked properly on an older os

https://www.reddit.com/r/raspberry_pi/comments/1lk18a7/35_lcd_touchscreen_for_raspberry_pi_3b/ 
used to help set up 3.5 LCD with drivers
/boot/config.txt edited (

#dtparam=i2c_arm=on
#dtparam=i2s=on
dtparam=spi=on

dtparam=audio=on

#/boot/firmware/overlays/README

#auto load overlays for dsi displays
display_auto_detect=1

#enable drivers
dtoverlay=vc4-kms-v3d
max_framebuffers=2

#run as fast as pi allows
arm_boost=1

[cm5]
dtoverlay=dwc2,dr_mode=host

[all]
dtoverlay=piscreen,speed=32000000,drm,swapxy=1,invy=0
max_framebuffers=2
hdmi_force_hotplug=1
enable_uart=1
)

<img width="608" height="728" alt="3 5 display connected" src="https://github.com/user-attachments/assets/2dcaab83-bea8-4ebf-a6fd-ba1886cb7455" />



https://github.com/user-attachments/assets/3cf342fe-9d2a-4035-985e-8595468f6288



useful resources used to help with understanding arduino/python code:

https://www.youtube.com/watch?v=BkZwxEueja8 
https://docs.arduino.cc/language-reference/en/functions/digital-io/digitalread/
https://docs.arduino.cc/learn/microcontrollers/digital-pins/ 
https://linux.die.net/man/5/xorg.conf  https://linux.die.net/man/4/evdev 
https://www.instructables.com/How-to-Make-a-Basic-Computer-Mouse-Using-the-Joyst/ 
https://python-evdev.readthedocs.io/en/latest/ 
https://python-evdev.readthedocs.io/en/latest/tutorial.html 
https://processing.org/reference/libraries/serial/Serial.html 
https://docs.kernel.org/input/uinput.html 
https://www.w3schools.com/python/default.asp 
https://www.youtube.com/watch?v=V_NXT2-QIlE 

Systemd file created to auto run controller code on boot

[Unit]
Description: Arduino controller
After=dev.ttyACM0.device
#waits for usb to be in port before starting

[Service]

Type=simple
#type simple so service starts immediately
#path to python code
#automatically will restart if service exits
#waits 2 seconds before restarting
#service ran as root since there are commands that need high permissions like keyboard inputs
#python output logs will be in journalctl to see errors

ExecStart=/usr/bin/python3 /home/cheeseits/testy2.py
Restart=always
RestartSec=2
User=root
Environment=PYTHONUNBUFFERED=1

[Install]
#systemd starts service during boot

WantedBy=multi-user.target
#ends here

Self note: 
in terminal enter nmtui for wifi connection
had issues with logging into pi had to forcibly go to tty1 screen to login
to go there: ctrl + alt + f1
<img width="608" height="771" alt="tty1 screen" src="https://github.com/user-attachments/assets/8c5cf30a-62c3-437d-a41d-264776546605" />
after entering username+password enter command startx to load desktop
<img width="581" height="768" alt="connection to linux terminal" src="https://github.com/user-attachments/assets/06b2a84b-8e76-4077-ba14-0a358a39436e" />

shell script created to run duck hunt through terminal commands/through files:

nano /home/cheeseits/duck_start.sh

#!/bin/bash 
Tells system that the script should be used to execute commands in the file

cd "/home/cheeseits/Downloads/project/Duck Hunt Style Game 2025"
mkdir -p bin
javac -d bin scr/*.java
java -cp bin Frame

#ends here

chmod +x /home/cheeseits/duck_start.sh
#makes file executable^
<img width="618" height="777" alt="video game connection" src="https://github.com/user-attachments/assets/d450fdb4-c8b4-492c-b265-54334541fccd" />

Visual Studio Code installed to run java code as Eclipse versions wouldn't run on dated os
