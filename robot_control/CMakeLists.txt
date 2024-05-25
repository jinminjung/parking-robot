cmake_minimum_required(VERSION 3.0.2)
project(robot_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
)

catkin_package()

install(PROGRAMS
  src/mecanum_drive.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
