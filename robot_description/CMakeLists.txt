cmake_minimum_required(VERSION 3.0.2)
project(robot_description)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES robot_description
#  CATKIN_DEPENDS joint_state_publisher robot_state_publisher
#  DEPENDS system_lib
)
