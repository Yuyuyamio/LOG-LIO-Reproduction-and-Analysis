#!/usr/bin/env bash
set -e

# LOG-LIO M2DGR door_02 reproduction helper.
# This script documents the two-terminal running procedure.
# Run the commands manually in the ROS Noetic Docker container.

echo "Terminal A: start LOG-LIO"
echo "cd /root/slam_ws"
echo "source /opt/ros/noetic/setup.bash"
echo "source devel/setup.bash"
echo "roslaunch log_lio mapping_m2dgr.launch rviz:=false"

echo ""
echo "Terminal B: play M2DGR door_02 rosbag"
echo "cd /root/slam_ws/datasets/M2DGR"
echo "source /opt/ros/noetic/setup.bash"
echo "rosbag play door_02.bag --topics /velodyne_points /handsfree/imu"
