#serial communication import reads data from arduino
#evdev library to access inputs like mouse
#UInput makes virtual input device
#ecodes as e access to input codes like x,y, and mouse clicks
import serial
import os
import time
from evdev import UInput, ecodes as e

#port arduino is connected to
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 115200

#deadzone variable where inputs are ignored so joystick input will only be read outside a certain area

DEADZONE = 50
SCALE = 0.01

#multiplied to joystick values to control speed

SHUTDOWN_TIME = 2.0

#ser object to read from the serial class
#serial port and baud rate timeout to wait for data

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

#uinput to make virtual mouse reading x,y, and clicks

ui = UInput({
    e.EV_REL: [e.REL_X, e.REL_Y],
    e.EV_KEY: [e.BTN_LEFT ,e.BTN_MIDDLE,e.BTN_RIGHT]
})


#message to see if code runs
print("Joystick On")

reed_start = None
shutdown_on = False

#try for inputs could interrupt code
try:
    while True:
#reading the new line with arduino input value number \n then converts bytes to strings strip removes spaces if not line skips lines without values
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue
#map function creates a range of values that are set to ints and separated by “,”
        try:
            x, y, clickBtn, btn,btn2  = map(int, line.split(","))
#deadzone checks if absolute value of x is greater than the deadzone then sends events to move mouse by x/y places

            if abs(x) > DEADZONE:
                ui.write(e.EV_REL, e.REL_X, int(-x * SCALE))

            if abs(y) > DEADZONE:
                ui.write(e.EV_REL, e.REL_Y, int(-y * SCALE))
#event type key for left button, clickBtn is value from arduino
                ui.write(e.EV_KEY, e.BTN_LEFT, clickBtn)
               	ui.write(e.EV_KEY, e.BTN_MIDDLE, joyBtn)
              	ui.write(e.EV_KEY,e.BTN_RIGHT,rBtn)

#reed switch connected to magnet shutdown won't start until timer activates
                if reed == 1 and not shutdown_on:
                    if reed_start is None:
                        #timer starts here
                        reed_start = time.time()
                        #if the magnet is connected for long enough it will shut down
                    elif time.time() - reed_start >= SHUTDOWN_TIME:
                        print("reed switch connected - shut down")
                    shutdown_on = True
                    #message sent to system to shutdown
                    os.system("sudo shutdown -h now")
                elif reed == 0:
                    reed_start = None
                #resets timer if the reed switch magnet is removed early
#sends events to system
                ui.syn()
#ignoring value error and continues reading inputs from loop
        except ValueError:
            pass

#ctrl c interrupt signal will stop program
except KeyboardInterrupt:
    print("Exit")
#closes virtual mouse and serial communication
finally:
    ui.close()
    ser.close()
