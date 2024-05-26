#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2, sqrt, cos, sin, pi

goal_angle_threshold = 0.1  # 목표 각도에 도달하는 임계값

theta = 0.0

def newOdom(msg):
    global theta

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def rotate_left(pub):
    global theta

    twist = Twist()
    r = rospy.Rate(4)

    # 목표 각도 계산 (현재 각도에서 90도를 더한 값)
    target_angle = theta - pi / 2 * 0.85

    while not rospy.is_shutdown():
        # 현재 각도와 목표 각도 사이의 각도 차이 계산
        angle_diff = target_angle - theta

        # Normalize the angle to the range [-pi, pi]
        while angle_diff > pi:
            angle_diff -= 2 * pi
        while angle_diff < -pi:
            angle_diff += 2 * pi

        # 목표 각도에 도달하면 회전을 멈추고 반복문을 종료
        if abs(angle_diff) < goal_angle_threshold:
            break

        # 로봇을 왼쪽으로 회전하도록 속도 설정
        twist.angular.z = -0.5 if angle_diff > 0 else -0.5

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
