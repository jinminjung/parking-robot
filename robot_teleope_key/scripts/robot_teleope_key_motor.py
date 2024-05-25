#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys, select, os
if os.name == 'nt':
  import msvcrt
else:
  import tty, termios
import RPi.GPIO as GPIO

ROBOT_MAX_LIN_VEL = 0.5
ROBOT_MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

msg = """
Control Your robot!
---------------------------
Moving around:
   q    w    e
   a    s    d
   z    x    c
w/x : increase/decrease linear_x velocity.
a/d : increase/decrease linear_y velocity.
q/e : increase/decrease angular velocity.
space key, s : force stop
CTRL-C to quit
"""

e = """
Communications Failed
"""
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

def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def vels(target_linear_vel, target_angular_vel):
    return "currently:\tlinear vel %s\t angular vel %s " % (target_linear_vel, target_angular_vel)

def makeSimpleProfile(output, input, slop):
    if input > output:
        output = min( input, output + slop )
    elif input < output:
        output = max( input, output - slop )
    else:
        output = input

    return output

def constrain(input, low, high):
    if input < low:
      input = low
    elif input > high:
      input = high
    else:
      input = input

    return input

def checkLinearLimitVelocity(vel):
    vel = constrain(vel, -ROBOT_MAX_LIN_VEL, ROBOT_MAX_LIN_VEL)
    return vel

def checkAngularLimitVelocity(vel):
    vel = constrain(vel, -ROBOT_MAX_ANG_VEL, ROBOT_MAX_ANG_VEL)
    return vel

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    status = 0
    target_linear_vel  = 0.0
    target_angular_vel   = 0.0
    control_linear_vel = 0.0
    control_angular_vel  = 0.0

    try:
        print(msg)
        while(1):
            twist = Twist()
            key = getKey()
            if key == 'w' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel + LIN_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (LIN_VEL_STEP_SIZE/2.0))
                twist.linear.x = control_linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
                pub.publish(twist)
                forward()
            elif key == 'x' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel - LIN_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (LIN_VEL_STEP_SIZE/2.0))
                twist.linear.x = control_linear_vel; twist.linear.y = 0.0; twist.linear.z = 0.0
                pub.publish(twist)
                backward()
            elif key == 'a' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel + LIN_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (LIN_VEL_STEP_SIZE/2.0))
                twist.linear.x = 0.0; twist.linear.y = control_linear_vel; twist.linear.z = 0.0
                pub.publish(twist)
                left()
            elif key == 'd' :
                target_linear_vel = checkLinearLimitVelocity(target_linear_vel - LIN_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_linear_vel = makeSimpleProfile(control_linear_vel, target_linear_vel, (LIN_VEL_STEP_SIZE/2.0))
                twist.linear.x = 0.0; twist.linear.y = control_linear_vel; twist.linear.z = 0.0
                pub.publish(twist)
                right()
            elif key == 'q' :
                target_angular_vel = checkAngularLimitVelocity(target_angular_vel + ANG_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_angular_vel = makeSimpleProfile(control_angular_vel, target_angular_vel, (ANG_VEL_STEP_SIZE/2.0))
                twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = control_angular_vel
                pub.publish(twist)
                turnleft()
            elif key == 'e' :
                target_angular_vel = checkAngularLimitVelocity(target_angular_vel - ANG_VEL_STEP_SIZE)
                status = status + 1
                print(vels(target_linear_vel,target_angular_vel))
                control_angular_vel = makeSimpleProfile(control_angular_vel, target_angular_vel, (ANG_VEL_STEP_SIZE/2.0))
                twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = control_angular_vel
                pub.publish(twist)
                turnright()
            elif key == ' ' or key == 's' :
                target_linear_vel   = 0.0
                control_linear_vel  = 0.0
                target_angular_vel  = 0.0
                control_angular_vel = 0.0
                print(vels(target_linear_vel, target_angular_vel))
                pub.publish(twist)
            else:
                if (key == '\x03'):
                    break

            if status == 20 :
                print(msg)
                status = 0

    except:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)

    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
