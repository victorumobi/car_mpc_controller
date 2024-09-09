#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

def generate_path():
    rospy.init_node('generate_path')
    path_pub = rospy.Publisher('path', Path, queue_size=10)
    rate = rospy.Rate(10)
    
    path = Path()
    path.header.frame_id = "map"
    
    # Generate a sample path
    for i in range(10):
        pose = PoseStamped()
        pose.header.frame_id = "map"
        pose.pose.position.x = i
        pose.pose.position.y = i
        pose.pose.orientation.w = 1.0
        path.poses.append(pose)
    
    while not rospy.is_shutdown():
        path_pub.publish(path)
        rate.sleep()

if __name__ == '__main__':
    try:
        generate_path()
    except rospy.ROSInterruptException:
        pass
