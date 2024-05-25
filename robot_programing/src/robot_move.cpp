#include <robot_programing/robot_move_function.h>

int main(int argc, char** argv) 
{
  ros::init(argc, argv, "robot_move"); 
  ros::NodeHandle n;

  robot my_robot(ros::this_node::getName());

  ////// robot programing control start //////

  my_robot.move_map(1.0, 3.0, 1.5708);
  
  my_robot.move_base(1.0, 3.0, 1.5708);

  ////// END //////

  return 0;
}
