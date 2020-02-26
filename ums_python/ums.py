import serial
import time
import wmi
import tkinter

import tkinter as tk

output = serial.Serial('COM3', 9600, timeout=.7)
time.sleep(1)

root = tk.Tk()
root.title('')

w = tk.Label(height = 3, width = 18, text="    Ulyu Monitoring System   \nRelease 1.0   26/02/2020",)
w.grid()

def close_window():
    time.sleep(1)
    output.write('Disconnected'.ljust(64).encode())
    root.destroy()

def red(): 
    output.write('red'.encode())

def green(): 
    output.write('green'.encode())

def blue(): 
    output.write('blue'.encode())

def redoff(): 
    output.write('redoff'.encode())

def greenoff(): 
    output.write('greenoff'.encode())

def blueoff(): 
    output.write('blueoff'.encode())


button = tk.Button (root, text = "Quit Ulyu MS", command = close_window)
button.grid(row=7)

color = tk.Label(text="RED:")
color.grid(row=3)
button = tk.Button (root, text = "ON", command = red)
button.grid(row=3, column=1)
button = tk.Button (root, text = "OFF", command = redoff)
button.grid(row=3, column=2)

color = tk.Label(text="GREEN:")
color.grid(row=4)
button = tk.Button (root, text = "ON", command = green)
button.grid(row=4, column=1)
button = tk.Button (root, text = "OFF", command = greenoff)
button.grid(row=4, column=2)

color = tk.Label(text="BLUE:")
color.grid(row=5)
button = tk.Button (root, text = "ON", command = blue)
button.grid(row=5, column=1)
button = tk.Button (root, text = "OFF", command = blueoff)
button.grid(row=5, column=2)

root.overrideredirect(1)

def update():
    global hwm
    hwm = wmi.WMI(namespace="root\OpenHardwareMonitor")
    global cpu
    global ram
    global disk
    hwm_data = hwm.Sensor()
    cpu = [] 
    ram = []
    disk = []
    
    for sensor in hwm_data:
        
        if sensor.SensorType==u'Temperature':
            if sensor.Name == u'CPU Package':
                cpu.insert(0,  "CPU temp : %d" % sensor.Value + "C")          

        if sensor.SensorType==u'Load':
            if sensor.Name == u'CPU Total':
                cpu.insert(1,  "CPU load : %d" % sensor.Value + "%")

        if sensor.SensorType==u'Load':
            if sensor.Name == u'Memory':
                ram.insert(0,  "RAM load : %d" % sensor.Value + "%")

        if sensor.SensorType==u'Load':
            if sensor.Name == u'Used Space':
                disk.insert(0,  "Disk space : %d" % sensor.Value + "%")

cpu = [] 
gpu = []
disk = []
    
while True:
    for i in range(4):
        update()
    root.update()
    output.write(cpu[0].ljust(16).encode())
    output.write(cpu[1].ljust(16).encode())
    output.write(ram[0].ljust(16).encode())
    output.write(disk[0].ljust(16).encode())
    time.sleep(0.5)
    


