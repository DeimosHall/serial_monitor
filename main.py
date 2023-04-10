#!/bin/python3
# Python script to print serial data from Arduino
from serial import Serial
import os

while True:
    ports = [port for port in os.listdir('/dev') if port.startswith('ttyUSB')]
    ports += [port for port in os.listdir('/dev') if port.startswith('ttyACM')]

    print("\nAvailable serial ports:")
    for i, port in enumerate(ports):
        print(f"{i}: {port}")

    print("e: Exit")
    print("r: Refresh")

    # Select serial port
    port_number = input('Select serial port: ')
    if port_number == 'e':
        break
    elif port_number == 'r':
        continue

    port = f"/dev/{ports[int(port_number)]}"

    # Open serial port
    ser = Serial(port, 115200)

    # Read and print data
    while True:
        try:
            line = ser.readline().decode('ascii', errors='ignore').rstrip()
            print(line)
        except KeyboardInterrupt:
            ser.close()
            break
