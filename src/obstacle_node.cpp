#include <ros/ros.h>
#include <geometry_msgs/PoseArray.h>

// Define your Obstacle Node

int main(int argc, char** argv) {
    ros::init(argc, argv, "obstacle_node");
    ros::NodeHandle nh;

    ros::Publisher obstacle_pub = nh.advertise<geometry_msgs::PoseArray>("obstacle_positions", 10);

    // Load or generate obstacles

    ros::Rate loop_rate(10);
    while (ros::ok()) {
        geometry_msgs::PoseArray obstacles;
        // Populate obstacle data
        obstacle_pub.publish(obstacles);
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
