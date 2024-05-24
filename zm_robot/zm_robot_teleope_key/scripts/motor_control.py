#!/usr/bin/env python3
# motor control code


# load the libraries
import RPi.GPIO as GPIO
import time
import numpy as np
import key_press as kp

#set GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# set variables for GPIO  Pins
pinMotorAForward = 9
pinMotorABackward = 10
pinMotorBForward = 8
pinMotorBBackward = 7
pinMotorCForward = 17
pinMotorCBackward = 27
pinMotorDForward = 23
pinMotorDBackward = 24





# PWM parameters
Frequency = 20
DutyCycleA = 70
DutyCycleB = 70
DutyCycleC = 50
DutyCycleD = 70
Stop = 0



# Set the GPIO Pin Mode
GPIO.setup(pinMotorAForward, GPIO.OUT)
GPIO.setup(pinMotorABackward, GPIO.OUT)
GPIO.setup(pinMotorBForward, GPIO.OUT)
GPIO.setup(pinMotorBBackward, GPIO.OUT)
GPIO.setup(pinMotorCForward, GPIO.OUT)
GPIO.setup(pinMotorCBackward, GPIO.OUT)
GPIO.setup(pinMotorDForward, GPIO.OUT)
GPIO.setup(pinMotorDBackward, GPIO.OUT)


# Set the GPIO to Software PWM at 'Frequency' Hertz
pwmMotorAForward = GPIO.PWM(pinMotorAForward, Frequency)
pwmMotorABackward = GPIO.PWM(pinMotorABackward, Frequency)
pwmMotorBForward = GPIO.PWM(pinMotorBForward, Frequency)
pwmMotorBBackward = GPIO.PWM(pinMotorBBackward, Frequency)
pwmMotorCForward = GPIO.PWM(pinMotorCForward, Frequency)
pwmMotorCBackward = GPIO.PWM(pinMotorCBackward, Frequency)
pwmMotorDForward = GPIO.PWM(pinMotorDForward, Frequency)
pwmMotorDBackward = GPIO.PWM(pinMotorDBackward, Frequency)


# set the duty cycle for software PWM - initially to 0
pwmMotorAForward.start(Stop)
pwmMotorABackward.start(Stop)
pwmMotorBForward.start(Stop)
pwmMotorBBackward.start(Stop)
pwmMotorCForward.start(Stop)
pwmMotorCBackward.start(Stop)
pwmMotorDForward.start(Stop)
pwmMotorDBackward.start(Stop)

def stopmotors():
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(Stop)

def forward():
    print('Moving Forward')
    pwmMotorAForward.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackward.ChangeDutyCycle(Stop)

def backward():
    print('Moving backward')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(DutyCycleB)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(DutyCycleD)

def left():
    print('Moving Left')
    pwmMotorAForward.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(DutyCycleB)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForward.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackward.ChangeDutyCycle(Stop)


def right():
    print('Moving Right')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForward.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(DutyCycleC)

def turnright():
    print('Turning Right')
    pwmMotorAForward.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(DutyCycleB)
    pwmMotorCForward.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(DutyCycleD)

def turnleft():
    print('Turning Left')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForward.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForward.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackward.ChangeDutyCycle(Stop)

def forwardleft():
    print('Moving Forward Left')
    pwmMotorAForward.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(DutyCycleD)
    pwmMotorDBackward.ChangeDutyCycle(Stop)    

def forwardright():
    print('Moving Forward Right')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(DutyCycleC)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(Stop)

def backwardleft():
    print('Moving Backward Left')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(Stop)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(DutyCycleB)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(DutyCycleC)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(Stop)

def backwardright():
    print('Moving Backward Right')
    pwmMotorAForward.ChangeDutyCycle(Stop)
    pwmMotorABackward.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForward.ChangeDutyCycle(Stop)
    pwmMotorBBackward.ChangeDutyCycle(Stop)
    pwmMotorCForward.ChangeDutyCycle(Stop)
    pwmMotorCBackward.ChangeDutyCycle(Stop)
    pwmMotorDForward.ChangeDutyCycle(Stop)
    pwmMotorDBackward.ChangeDutyCycle(DutyCycleD)

def key_control():

    if kp.getKey('a'):
        left()

    elif kp.getKey('d'):
        right()
        
    elif kp.getKey('w'):
        forward()
        
    elif kp.getKey('x'):
        backward()

    elif kp.getKey('t'):
        turnright()
    
    elif kp.getKey('r'):
        turnleft()
    
    elif kp.getKey('q'):
        forwardleft()
    
    elif kp.getKey('e'):
        forwardright()
    
    elif kp.getKey('z'):
        backwardleft()
    
    elif kp.getKey('c'):
        backwardright()

    elif kp.getKey('ESCAPE'):
        stopmotors()
        kp.stop()
        GPIO.cleanup()

    else:
        stopmotors()
        

def exec_cmd(cmd_str):
    if cmd_str == 'a':
        left()
        print('Moving Left')
    elif cmd_str == 'd':
        right()
        print('Moving Right')
    elif cmd_str == 'w':
        forward()
        print('Moving Forward')
    elif cmd_str == 'x':
        backward()
        print('Moving Backward')
    elif cmd_str == 'r':
        turnleft()
        print('Turning Left')
    elif cmd_str == 't':
        turnright()
        print('Turning Right')
    elif cmd_str == 'q':
        forwardleft()
        print('Moving Forward Left')
    elif cmd_str == 'e':
        forwardright()
        print('Moving Forward Right')
    elif cmd_str == 'z':
        backwardleft()
        print('Moving Backward Left')
    elif cmd_str == 'c':
        backwardright()
        print('Moving Backward Right')
    else:
        stopmotors()
        
    

if __name__ == '__main__':
    stopmotors()
    kp.init()
    print('Controlling using keyboard')
    while True:
        try:
            key_control()
        except KeyboardInterrupt:
            GPIO.cleanup()
    


