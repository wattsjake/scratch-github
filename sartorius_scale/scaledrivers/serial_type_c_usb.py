import csv
import numpy as np
import serial 

import matplotlib.pyplot as plt
import numpy as np
from scale import Scale


        

# tare = b'\x1BU'
# print_screen = b'\x1BP'
# zero = b'\x1Bf3_'
# sound = b'\x1BQ'

# def connect():
#     print('connecting to device')
#     try:
#         ser = serial.Serial(
#                             port='COM4',\
#                             baudrate=115200,\
#                             parity=serial.PARITY_NONE,\
#                             stopbits=serial.STOPBITS_ONE,\
#                             bytesize=serial.EIGHTBITS,\
#                             timeout=4)
#         print("connected to: " + ser.portstr)
    
#     except serial.serialutil.SerialException:
#         print("The port is in use. Unplug USB-C")  
#     return ser
  
# def serial_send(parameter,ser):
#     try:
#         ser.write(parameter)
#         print("Serial Send %s" %parameter)
#     except NameError as e:
#         print('[Error]Connect to scale')

# def main():
#     ser = connect()
#     ser.write(zero)
#     ser.write(sound)

#     while(True):
#         print(chr(ser.read()))
    

# if __name__ == "__main__":
#      main()


