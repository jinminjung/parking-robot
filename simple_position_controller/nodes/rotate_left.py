#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import pi

theta = 0.0

def newOdom(msg):
    global theta

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def rotate_left(pub):
    twist = Twist()
    r = rospy.Rate(10)  # 10Hz

    # 로봇을 왼쪽으로 회전하도록 속도 설정
    twist.angular.z = 0.5

    start_time = rospy.Time.now()
    duration = rospy.Duration(4)  # 4초 동안 회전

    while rospy.Time.now() - start_time < duration:
        pub.publish(twist)
        r.sleep()

    # 회전을 멈추기 위해 속도를 0으로 설정하고 발행
    twist.angular.z = 0.0
    pub.publish(twist)

if __name__ == "__main__":
    rospy.init_node('turtlebot3_rotate')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("/odom", Odometry, newOdom)

    rospy.sleep(1)  # 초기화를 위한 시간 제공

    rotate_left(pub)
