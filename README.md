# ConsoleCapstone-MM-JC
Michael Monrroy's and Julius Conception's Capstone Project
!
Design process: 
Initial problem: 
The problem is that game consoles run out of battery too soon and screen glare makes usage of the console difficult outdoors. We’d use solar energy to power our console when there’s a light source similar to a battery. The console would be able to be powered by a rechargeable battery as well so at night the console would switch energy sources.

But our main focus switched to creating an interface that can select and play different games that is controlled by a joystick, buttons, and is displayed on a screen


Usage of Ms Hester's Arduino kit was used to build a foundational understanding of how LCD's and inputs work with Arduino

<img width="412" height="416" alt="Screenshot 2026-01-14 11 26 12 AM" src="https://github.com/user-attachments/assets/1e6a0283-b505-4748-9a9f-8bedbd9a0418" />
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
after entering username+password enter command startx to load desktop

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

Visual Studio Code installed to run java code as Eclipse versions wouldn't run on dated os


