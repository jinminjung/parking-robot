#!/usr/bin/env python3

import serial
import time

def send_command(command):
    ser = serial.Serial('/dev/ttyACM0', 9600)  # '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1' 등으로 변경 가능
    time.sleep(2)  # 안정화 대기
    ser.write(command.encode())
    time.sleep(0.1)
    ser.close()

send_command('U')
