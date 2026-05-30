# LOG-LIO Reproduction Run Notes: M2DGR door_02

## Environment

Platform: WSL2 Ubuntu + Docker  
ROS version: ROS Noetic  
Docker image backup: loglio_noetic_built:v1  
Workspace: /root/slam_ws  
Package: log_lio  

## Build Status

LOG-LIO was successfully compiled inside the Docker container.

Key executable generated:

/root/slam_ws/devel/lib/log_lio/loglio_mapping

The ROS package was also successfully found using:

rospack find log_lio

## Dataset

Dataset used:

M2DGR door_02.bag

Rosbag information:

duration: 127 s  
size: 9.8 GB  
messages: 188889  

Required topics were confirmed:

/velodyne_points  
/handsfree/imu  

These topics match the LOG-LIO M2DGR configuration:

LiDAR topic: /velodyne_points  
IMU topic: /handsfree/imu  

## Run Commands

Terminal A:

cd /root/slam_ws  
source /opt/ros/noetic/setup.bash  
source devel/setup.bash  
roslaunch log_lio mapping_m2dgr.launch rviz:=false  

Terminal B:

cd /root/slam_ws/datasets/M2DGR  
source /opt/ros/noetic/setup.bash  
rosbag play door_02.bag --topics /velodyne_points /handsfree/imu  

## Output

The run completed successfully.

Generated result files:

Log/target_path.txt  
Log/pos_log.txt  
Log/fast_lio_time_log.csv  

The main trajectory output was copied to:

results/door_02_run1/target_path.txt

Trajectory line count:

2469

The first timestamp in target_path.txt is approximately:

1628062054.8588

The last timestamp is approximately:

1628062181.7062

This confirms that LOG-LIO processed the full door_02 sequence and produced a trajectory result.
