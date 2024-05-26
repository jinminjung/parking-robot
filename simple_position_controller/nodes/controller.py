#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2, sqrt, cos, sin

x = 0.0
y = 0.0 
theta = 0.0

def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odometry/filtered", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

speed = Twist()

r = rospy.Rate(4)

goal = Point()
goal.x = 0
goal.y = 0.5

while not rospy.is_shutdown():
    inc_x = goal.x - x
    inc_y = goal.y - y

    distance_to_goal = sqrt(inc_x**2 + inc_y**2)
    angle_to_goal = atan2(inc_y, inc_x)

    # Calculate the error in orientation
    angle_diff = angle_to_goal - theta

    # Normalize the angle to the range [-pi, pi]
    while angle_diff > 3.14:
        angle_diff -= 2 * 3.14
    while angle_diff < -3.14:
        angle_diff += 2 * 3.14

    if distance_to_goal > 0.1:  # Check if the robot is close to the goal
        speed.linear.x = 0.5 * cos(angle_diff) * min(distance_to_goal, 1)  # Move towards the goal in the x direction
        speed.linear.y = 0.5 * sin(angle_diff) * min(distance_to_goal, 1)  # Move towards the goal in the y direction
        speed.angular.z = 0.3 * angle_diff  # Adjust orientation
    else:
        speed.linear.x = 0.0
        speed.linear.y = 0.0
        speed.angular.z = 0.0
        

    pub.publish(speed)
    r.sleep()
