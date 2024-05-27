#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import os

ROBOT_MAX_LIN_VEL = 0.5

def move_left_for_seconds(pub, seconds, speed):
    twist = Twist()
    twist.linear.y = speed
    r = rospy.Rate(10)  # 10Hz

    start_time = rospy.Time.now()
    duration = rospy.Duration(seconds)

    while rospy.Time.now() - start_time < duration:
        pub.publish(twist)
        r.sleep()

    # 멈추기 위해 속도를 0으로 설정하고 발행
    twist.linear.y = 0.0
    pub.publish(twist)

if __name__=="__main__":
    rospy.init_node('turtlebot3_teleop')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rospy.sleep(1)  # 초기화를 위한 시간 제공

    try:
        move_left_for_seconds(pub, 4, 0.5)  # 4초 동안 y 방향으로 이동

    except Exception as e:
        print("Error:", e)

    finally:
        twist = Twist()
        twist.linear.x = 0.0; twist.linear.y = 0.0; twist.linear.z = 0.0
        twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = 0.0
        pub.publish(twist)
