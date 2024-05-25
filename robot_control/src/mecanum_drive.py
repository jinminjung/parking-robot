#!/usr/bin/env python3

import RPi.GPIO as GPIO
import rospy
from geometry_msgs.msg import Twist

# GPIO 핀 번호 정의
MOTOR_PINS = {
    'FL': {'ENA': 17, 'IN1': 22, 'IN2': 23},
    'FR': {'ENA': 18, 'IN3': 24, 'IN4': 25},
    'BL': {'ENA': 27, 'IN1': 5,  'IN2': 6},
    'BR': {'ENA': 13, 'IN3': 19, 'IN4': 26}
}

def setup_motor_pins():
    GPIO.setmode(GPIO.BCM)
    for motor in MOTOR_PINS.values():
        GPIO.setup(motor['ENA'], GPIO.OUT)
        GPIO.setup(motor['IN1'], GPIO.OUT)
        GPIO.setup(motor['IN2'], GPIO.OUT)
        motor['pwm'] = GPIO.PWM(motor['ENA'], 1000)  # 1kHz 주파수
        motor['pwm'].start(0)

def set_motor_speed(motor, speed):
    if speed > 0:
        GPIO.output(motor['IN1'], GPIO.HIGH)
        GPIO.output(motor['IN2'], GPIO.LOW)
    elif speed < 0:
        GPIO.output(motor['IN1'], GPIO.LOW)
        GPIO.output(motor['IN2'], GPIO.HIGH)
    else:
        GPIO.output(motor['IN1'], GPIO.LOW)
        GPIO.output(motor['IN2'], GPIO.LOW)
    motor['pwm'].ChangeDutyCycle(abs(speed))

def mecanum_drive(x, y, rot):
    # 속도 계산
    fl_speed = x - y - rot
    fr_speed = x + y + rot
    bl_speed = x + y - rot
    br_speed = x - y + rot

    # 속도 설정
    set_motor_speed(MOTOR_PINS['FL'], fl_speed * 100)
    set_motor_speed(MOTOR_PINS['FR'], fr_speed * 100)
    set_motor_speed(MOTOR_PINS['BL'], bl_speed * 100)
    set_motor_speed(MOTOR_PINS['BR'], br_speed * 100)

def cmd_vel_callback(msg):
    x = msg.linear.x
    y = msg.linear.y
    rot = msg.angular.z
    mecanum_drive(x, y, rot)

def main():
    rospy.init_node('mecanum_drive_node')
    setup_motor_pins()
    rospy.Subscriber('/cmd_vel', Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
    finally:
        for motor in MOTOR_PINS.values():
            motor['pwm'].stop()
        GPIO.cleanup()
