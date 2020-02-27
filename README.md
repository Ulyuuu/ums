# ums
Ums (ulyu monitoring system) is a system allowing to display in real time the temperature, voltage and frequency sensors of a computer on a screen coupled to an arduino. 
Ums works with Open Hradware Monitor and a program in python. It's also able to controlling a simple rgb led strip (the color will be the same over the entire length) with a very simple but functional control panel. 
In my case, I am not using aduino but directly the ATMega328p chip on a pcb (The components which are around the chip and the FTDI (the red plate between the USB and the circuit) will not be necessary if you only used one arduino and the two 16x2 screens)

![alt text](https://github.com/Ulyuuu/ums/blob/master/Github_images/IMG_0388.JPG)



Required components :
- [2] 16x2 lcd arduino display
- [2] 50Kohms potentiometer
- (Optional) RGB strip with the controller
- Arduino (all version work)
  OR
  Atmega328p (the chip i'm using) with
    - [2] 22pf capacitor
    - 10Kohms resistor
    - 16Mhz quartz
    - FTDI board for usb interface

Scehmatics :

/!\ Ground and vcc of the lcd aren't connected to the arduino but they must be !

![alt text](https://github.com/Ulyuuu/ums/blob/master/Github_images/arduino_schematic.png)

With the ATMega328p the circuit is the same but you need to connect the FTDI board to Reset, RX and TX

![alt text](https://github.com/Ulyuuu/ums/blob/master/Github_images/atmega328p.jpg)

/!\ If you wand to use the color controller, red is connected to pin 11, green to pin 12 and blue to pin 13

Utilization :

1: Connect arduino to pc
2: televerse arduino code (ums_arduino/ums.ino)
3: Install all the python librairies  (Install part)
4: Edit the python program (ums_python/ums.py)
5: Locate "output = serial.Serial('COM3', 9600, timeout=.7)" and change 'COM3' by the port your arduino is curently using
6: Save program
7: Open OpenHradwareMonitor (download it from https://openhardwaremonitor.org/files/openhardwaremonitor-v0.9.1.zip)
8: Open python program
9: Done ! you cane now change strip's color if you connect it to the arduino and you can quit Ums 

![alt text](https://github.com/Ulyuuu/ums/blob/master/Github_images/ums_program.png)
