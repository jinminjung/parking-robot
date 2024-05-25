#include "safety/safety.h"

int main(int argc, char** argv)
{
	ros::init(argc, argv, "safety_node");

	Safety rs;
	rs.spin();

	return 0;
}