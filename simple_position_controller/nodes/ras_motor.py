#!/usr/bin/env python3

import serial
import time

# 시리얼 포트 경로를 실제 연결된 장치 경로로 변경
ser = serial.Serial('/dev/ttyACM0', 9600)  # '/dev/ttyACM1', '/dev/ttyUSB0', '/dev/ttyUSB1' 등으로 변경 가능
time.sleep(2)  # 안정화 대기

def send_command(command):
    ser.write(command.encode())
    time.sleep(0.1)

# 초기 버퍼 정리
ser.reset_input_buffer()

while True:
    if ser.in_waiting > 0:
        try:
            raw_data = ser.readline()
            message = raw_data.decode().strip()
            if message == "LIFT_RAISED":
                print("리프트가 상승되었습니다.")
            elif message == "LIFT_DOWN":
                print("리프트가 하강되었습니다.")
                # 여기에 시작 좌표로 복귀하는 코드를 추가
            elif message == "대기 상태로 돌아갑니다. liftDirection: ":
                print("입/출차 대기상태 입니다.")
        except UnicodeDecodeError:
            print("수신된 데이터가 UTF-8로 디코딩되지 않았습니다: {raw_data}")
    
    time.sleep(0.1)

