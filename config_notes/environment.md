# Environment Notes

## Setup

| Item       | Setting               |
| ---------- | --------------------- |
| Host       | Windows + WSL2 Ubuntu |
| Runtime    | Docker container      |
| ROS        | Noetic                |
| Build      | catkin                |
| Dataset    | M2DGR `door_02`       |
| Evaluation | evo                   |

LOG-LIO was built and tested inside the ROS Noetic Docker container.
This repository only stores reproduction notes, results, figures, and analysis documents.

## Workspace

```text
/root/slam_ws
```

Large dataset files such as `.bag` are excluded from this repository.

## Run

```bash
roslaunch log_lio mapping_m2dgr.launch rviz:=false
rosbag play door_02.bag --topics /velodyne_points /handsfree/imu
```

## Notes

Build issues are recorded in:

```text
troubleshooting/ros_build_errors.md
```

RViz was disabled during the main run to avoid display issues in the WSL/Docker environment.
