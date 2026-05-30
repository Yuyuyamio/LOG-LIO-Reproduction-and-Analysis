# LOG-LIO Result Analysis: M2DGR door_02

## 1. Purpose of This Run

This run was used to verify whether LOG-LIO can be built, launched, and executed on a real M2DGR rosbag sequence. The selected sequence was `door_02`, which contains both LiDAR and IMU topics required by the LOG-LIO M2DGR configuration.

The purpose of this stage was not to perform final benchmark evaluation yet. Instead, the main goal was to check whether the system can produce a complete odometry trajectory from real sensor data.

## 2. Input Data

The rosbag used in this run was:

- Dataset: M2DGR
- Sequence: door_02
- Duration: about 127 s
- Size: about 9.8 GB

The required topics were confirmed using `rosbag info`:

- LiDAR topic: `/velodyne_points`
- IMU topic: `/handsfree/imu`

These topics match the LOG-LIO configuration in `config/velodyne_m2dgr.yaml`.

## 3. Running Configuration

The LOG-LIO node was launched using:

roslaunch log_lio mapping_m2dgr.launch rviz:=false

The rosbag was played with only the required topics:

rosbag play door_02.bag --topics /velodyne_points /handsfree/imu

RViz was disabled during this run because the Docker environment was mainly used for command-line reproduction. This avoided display-related problems and allowed the focus to stay on whether the odometry pipeline itself could run.

## 4. Output Files

The run generated several output files in the LOG-LIO `Log` directory, including:

- `target_path.txt`
- `pos_log.txt`
- `fast_lio_time_log.csv`

The main trajectory file used for analysis was:

results/door_02_run1/target_path.txt

This file contains 2469 valid trajectory rows. Each row follows the format:

timestamp x y z qx qy qz qw

This means each output entry stores the estimated position and orientation of the platform at a specific timestamp.

## 5. Trajectory Sanity Check

The first trajectory timestamp was approximately:

1628062054.8588

The last trajectory timestamp was approximately:

1628062181.7062

This shows that the trajectory covers almost the full time range of the `door_02` rosbag.

The estimated position changed continuously during the run. This is important because it shows that LOG-LIO did not simply start and exit. It processed the incoming LiDAR and IMU data and produced a time-continuous odometry result.

## 6. Qualitative Interpretation

The XY trajectory visualization gives a direct view of the horizontal motion estimated by LOG-LIO. Since the start and end positions are different and the trajectory contains many intermediate poses, the result can be treated as a valid first reproduction output.

The z-position plot is used to check the vertical motion trend. At this stage, the plot is mainly used for sanity checking rather than final accuracy evaluation. A reasonable z trend suggests that the odometry output is not completely unstable.

## 7. Current Limitation

This result does not yet prove the final accuracy of LOG-LIO, because no ground-truth trajectory has been compared in this stage. The current analysis only confirms that:

- the package builds successfully,
- the M2DGR configuration loads correctly,
- the correct LiDAR and IMU topics are consumed,
- the full bag sequence is processed,
- a complete trajectory output is generated.

A later stage should compare the estimated trajectory with ground truth or a reference result if available.

## 8. Conclusion

This run successfully reproduced the basic LOG-LIO pipeline on the M2DGR `door_02` sequence. The system generated a complete trajectory file and supporting runtime logs. The result is sufficient for the current reproduction stage and can be used for further visualization, trajectory comparison, and method-level analysis.
