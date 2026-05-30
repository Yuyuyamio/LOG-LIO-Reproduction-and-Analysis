# M2DGR Configuration Notes

## Tested Sequence

| Item            | Value     |
| --------------- | --------- |
| Dataset         | M2DGR     |
| Sequence        | `door_02` |
| Rosbag duration | 127 s     |
| Rosbag size     | 9.8 GB    |

## Required Topics

| Sensor | Topic              |
| ------ | ------------------ |
| LiDAR  | `/velodyne_points` |
| IMU    | `/handsfree/imu`   |

These two topics were confirmed with `rosbag info` before running LOG-LIO.

## LOG-LIO Files Used

| Type        | File                          |
| ----------- | ----------------------------- |
| Launch file | `launch/mapping_m2dgr.launch` |
| Config file | `config/velodyne_m2dgr.yaml`  |

## Run Setting

RViz was disabled during the main run:

`roslaunch log_lio mapping_m2dgr.launch rviz:=false`

The rosbag was played with only the required topics:

`rosbag play door_02.bag --topics /velodyne_points /handsfree/imu`

## Notes

The run generated `target_path.txt`, `pos_log.txt`, and `fast_lio_time_log.csv`.

The ground-truth text file used for evaluation provides valid position values, but its quaternion fields are all zeros. Therefore, the current evo evaluation is treated as position-based trajectory evaluation.
