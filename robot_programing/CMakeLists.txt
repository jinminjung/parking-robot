cmake_minimum_required(VERSION 3.0.2)
project(robot_programing)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  message_generation
  move_base_msgs
  roscpp
  sensor_msgs
  std_msgs
  tf
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

generate_messages(
   DEPENDENCIES
   std_msgs  
 )

catkin_package(

)

add_executable(robot_move src/robot_move_action.cpp src/robot_move.cpp)
target_link_libraries(robot_move ${catkin_LIBRARIES})
add_dependencies(robot_move robot_programing_generate_messages_cpp)
