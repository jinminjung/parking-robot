cmake_minimum_required(VERSION 3.0.2)
project(robot_safety)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  geometry_msgs
  laser_geometry
  sensor_msgs
  std_msgs
  tf
  visualization_msgs
)

generate_dynamic_reconfigure_options(
  cfg/safety.cfg
)

catkin_package(
   INCLUDE_DIRS include
#  LIBRARIES safety
   CATKIN_DEPENDS dynamic_reconfigure geometry_msgs laser_geometry sensor_msgs std_msgs tf visualization_msgs
#  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${laser_geometry_INCLUDE_DIRS}
)

add_executable(safety_node src/safety_node.cpp src/safety.cpp)
target_link_libraries(safety_node ${catkin_LIBRARIES})
add_dependencies(safety_node robot_safety_gencfg)
