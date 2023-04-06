#!/bin/python3
# Python script to print serial data from Arduino
from serial import Serial
import os

while True:
    ports = [port for port in os.listdir('/dev') if port.startswith('ttyUSB')]
    ports += [port for port in os.listdir('/dev') if port.startswith('ttyACM')]

    print("Available serial ports:")
    for i, port in enumerate(ports):
        print(f"{i}: {port}")

    # Select serial port
    port = f"/dev/{ports[int(input('Select serial port: '))]}"

    # Open serial port
    ser = Serial(port, 115200)

    # Read and print data
    while True:
        try:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        except KeyboardInterrupt:
            ser.close()
            break
