# LOG-LIO Reproduction and Analysis

This repository documents my reproduction and analysis of LOG-LIO, a LiDAR-Inertial Odometry system with efficient local geometric information estimation.

## Repository Strategy

This repository is organized as a reproduction-oriented project rather than a direct fork of the official LOG-LIO repository. The official LOG-LIO code will be cloned locally for building and testing, while this repository mainly records my reproduction notes, environment setup, scripts, results, figures, and final report.

The goal of this project is not to propose a new SLAM algorithm, but to understand how LOG-LIO uses local geometric information, including normal estimation, point distribution, and hierarchical data association, to improve LiDAR-inertial odometry.

## Project Goals

- Understand the core method of LOG-LIO
- Reproduce LOG-LIO on selected M2DGR sequences
- Evaluate the reproduced trajectory using ATE and RPE
- Analyze successful and failed cases
- Document ROS, dataset, and evaluation issues

## Current Stage

This repository is currently in the early reproduction stage. I first organize the paper understanding, project structure, and experimental plan before running the full SLAM system.

## Planned Outputs

- Paper notes
- Method explanation
- Reproduction scripts
- M2DGR experiment results
- Trajectory comparison figures
- ATE / RPE evaluation results
- Troubleshooting records
- Final reproduction report
---

## Current Reproduction Status

This repository currently documents a successful LOG-LIO reproduction workflow on the M2DGR `door_02` sequence.

### Completed Work

- Set up a ROS Noetic environment using WSL2 Ubuntu and Docker.
- Built LOG-LIO successfully inside the Docker container.
- Fixed missing ROS/PCL/OpenCV-related build dependencies.
- Generated the main executable:

  /root/slam_ws/devel/lib/log_lio/loglio_mapping

- Verified that the ROS package can be found using `rospack find log_lio`.
- Downloaded and checked the M2DGR `door_02.bag` sequence.
- Confirmed the required rosbag topics:

  /velodyne_points  
  /handsfree/imu

- Ran LOG-LIO on the full `door_02` sequence using:

  roslaunch log_lio mapping_m2dgr.launch rviz:=false

- Generated trajectory output:

  results/door_02_run1/target_path.txt

- Performed trajectory sanity checking.
- Generated trajectory visualization files.
- Added runtime log analysis based on `fast_lio_time_log.csv`.
- Added method-to-code mapping notes for the main LOG-LIO modules.

### Main Result Files

The main reproduction result files are located in:

results/door_02_run1/

Important files include:

- target_path.txt
- pos_log.txt
- fast_lio_time_log.csv
- trajectory_sanity_check.md
- trajectory_xy.svg
- trajectory_z_time.svg
- run_summary.txt

### Main Documentation Files

Important documentation files include:

- docs/door_02_run_notes.md
- docs/door_02_result_analysis.md
- docs/trajectory_visualization_notes.md
- docs/runtime_log_analysis.md
- docs/method_to_code_mapping.md
- troubleshooting/ros_build_errors.md

### Current Understanding

The current reproduction confirms that LOG-LIO can be built and executed on a real M2DGR rosbag sequence. The system successfully consumes LiDAR and IMU topics, processes the sequence, and produces a continuous trajectory output.

The project has now moved beyond simple build verification. It includes environment setup, build troubleshooting, full rosbag execution, trajectory output checking, runtime log analysis, and source-code-level method mapping.

---

## Current Reproduction Status

This repository currently documents a successful LOG-LIO reproduction workflow on the M2DGR `door_02` sequence.

### Completed Work

- Set up a ROS Noetic environment using WSL2 Ubuntu and Docker.
- Built LOG-LIO successfully inside the Docker container.
- Fixed missing ROS/PCL/OpenCV-related build dependencies.
- Generated the main executable:

  /root/slam_ws/devel/lib/log_lio/loglio_mapping

- Verified that the ROS package can be found using `rospack find log_lio`.
- Downloaded and checked the M2DGR `door_02.bag` sequence.
- Confirmed the required rosbag topics:

  /velodyne_points  
  /handsfree/imu

- Ran LOG-LIO on the full `door_02` sequence using:

  roslaunch log_lio mapping_m2dgr.launch rviz:=false

- Generated trajectory output:

  results/door_02_run1/target_path.txt

- Performed trajectory sanity checking.
- Generated trajectory visualization files.
- Added runtime log analysis based on `fast_lio_time_log.csv`.
- Added method-to-code mapping notes for the main LOG-LIO modules.

### Main Result Files

The main reproduction result files are located in:

results/door_02_run1/

Important files include:

- target_path.txt
- pos_log.txt
- fast_lio_time_log.csv
- trajectory_sanity_check.md
- trajectory_xy.svg
- trajectory_z_time.svg
- run_summary.txt

### Main Documentation Files

Important documentation files include:

- docs/door_02_run_notes.md
- docs/door_02_result_analysis.md
- docs/trajectory_visualization_notes.md
- docs/runtime_log_analysis.md
- docs/method_to_code_mapping.md
- troubleshooting/ros_build_errors.md

### Current Understanding

The current reproduction confirms that LOG-LIO can be built and executed on a real M2DGR rosbag sequence. The system successfully consumes LiDAR and IMU topics, processes the sequence, and produces a continuous trajectory output.

The project has now moved beyond simple build verification. It includes environment setup, build troubleshooting, full rosbag execution, trajectory output checking, runtime log analysis, and source-code-level method mapping.
