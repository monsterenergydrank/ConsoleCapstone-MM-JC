# ConsoleCapstone-MM-JC
Michael Monrroy's and Julius Conception's Capstone Project
!
Work done to ensure the display would connect
https://www.reddit.com/r/raspberry_pi/comments/1lk18a7/35_lcd_touchscreen_for_raspberry_pi_3b/ 
used to help set up 3.5 LCD with drivers
/boot/config.txt edited

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
