#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2, sqrt, cos, sin
import sys, select, os

if os.name == 'nt':
    import msvcrt
else:
    import tty, termios

ROBOT_MAX_LIN_VEL = 0.5
ROBOT_MAX_ANG_VEL = 1.82

LIN_VEL_STEP_SIZE = 0.01
ANG_VEL_STEP_SIZE = 0.1

goal_distance_threshold = 0.1  # 목표 지점 도착 거리 임계값

x = 0.0
y = 0.0 
theta = 0.0

def newOdom(msg):
    global x, y, theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

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

if __name__ == "__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("/odom", Odometry, newOdom)

    goal_x = -1
    goal_y = 0

    twist = Twist()
    r = rospy.Rate(4)

    try:
        while not rospy.is_shutdown():
            # 현재 위치와 목표 위치 간의 거리 계산
            inc_x = goal_x - x
            inc_y = goal_y - y
            distance_to_goal = sqrt(inc_x**2 + inc_y**2)

            # 목표 위치까지의 각도 계산
            angle_to_goal = atan2(inc_y, inc_x)

            # 현재 로봇의 방향과 목표 방향 사이의 각도 차이 계산
            angle_diff = angle_to_goal - theta

            # Normalize the angle to the range [-pi, pi]
            while angle_diff > 3.14:
                angle_diff -= 2 * 3.14
            while angle_diff < -3.14:
                angle_diff += 2 * 3.14

            # 목표지점 도착 여부 확인
            if distance_to_goal > goal_distance_threshold:
                twist.linear.x = 0.5 * cos(angle_diff) * min(distance_to_goal, 1)  # x 방향으로의 속도
                twist.linear.y = 0.5 * sin(angle_diff) * min(distance_to_goal, 1)  # y 방향으로의 속도
                twist.angular.z = 0.3 * angle_diff  # 로봇의 방향 조절
            else:
                # 목표 지점에 도착하면 로봇을 정지
                twist.linear.x = 0.0
                twist.linear.y = 0.0
                twist.angular.z = 0.0

            pub.publish(twist)
            r.sleep()

    except Exception as e:
        print(e)

    finally:
        if os.name != 'nt':
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
