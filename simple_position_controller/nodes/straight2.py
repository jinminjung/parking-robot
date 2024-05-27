#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

if __name__ == "__main__":
    rospy.init_node('turtlebot3_straight')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    twist = Twist()
    twist.linear.x = 0.5  # 로봇의 직진 속도 설정 (m/s)
    twist.linear.y = 0.0
    twist.angular.z = 0.0

    start_time = time.time()
    rate = rospy.Rate(10)  # 10Hz로 퍼블리시

    while not rospy.is_shutdown() and time.time() - start_time < 2:  # 5초 동안 움직임
        pub.publish(twist)
        rate.sleep()

    # 로봇 정지
    twist.linear.x = 0.0
    pub.publish(twist)