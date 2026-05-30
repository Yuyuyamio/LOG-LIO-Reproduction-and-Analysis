# LOG-LIO Reproduction and Analysis

A reproduction and code-level analysis of **LOG-LIO**, a LiDAR-Inertial Odometry system focused on efficient local geometric information estimation.

This repository is not an algorithm modification project. Its goal is to reproduce LOG-LIO on a real ground-robot dataset, inspect its implementation, and understand how local geometry is used in LiDAR-inertial odometry.

## What This Repository Contains

* Built LOG-LIO in a ROS Noetic Docker environment.
* Ran LOG-LIO on the M2DGR `door_02` sequence.
* Verified LiDAR and IMU topic compatibility:

  * `/velodyne_points`
  * `/handsfree/imu`
* Generated a complete trajectory output with 2469 poses.
* Performed trajectory visualization and evo-based APE/RPE evaluation.
* Analyzed runtime logs from `fast_lio_time_log.csv`.
* Mapped the main algorithm modules to source code files.

## Method Overview

LOG-LIO improves LiDAR-inertial odometry by using local geometric information more efficiently.

The reproduced pipeline can be summarized as:

```text
LiDAR + IMU
   ↓
IMU processing and scan undistortion
   ↓
Ring FALS normal estimation
   ↓
Voxel map / extended ikd-tree maintenance
   ↓
Point distribution update
   ↓
Hierarchical data association
   ├── point-to-surfel
   └── point-to-plane fallback
   ↓
Pose optimization
   ↓
Odometry trajectory
```

The main method components studied in this project are:

| Component                   | Role                                                                                |
| --------------------------- | ----------------------------------------------------------------------------------- |
| Ring FALS normal estimation | Estimates local surface normals using LiDAR ring and range-image structure          |
| Voxel / ikd-tree map        | Maintains local map and voxel-level point distribution                              |
| Hierarchical association    | Uses surfel constraints when reliable and falls back to plane constraints otherwise |
| Iterated state update       | Uses geometric residuals to update the LiDAR-IMU state                              |

## Reproduction Setup

| Item         | Configuration          |
| ------------ | ---------------------- |
| OS           | WSL2 Ubuntu            |
| Container    | Docker                 |
| ROS          | ROS Noetic             |
| Build system | catkin                 |
| Dataset      | M2DGR `door_02`        |
| LiDAR topic  | `/velodyne_points`     |
| IMU topic    | `/handsfree/imu`       |
| Launch file  | `mapping_m2dgr.launch` |
| Config file  | `velodyne_m2dgr.yaml`  |



## Dataset

This reproduction uses one selected M2DGR sequence instead of the full dataset.

| Sequence  | Duration |   Size | Status                 |
| --------- | -------: | -----: | ---------------------- |
| `door_02` |    127 s | 9.8 GB | Successfully processed |

The rosbag was checked with `rosbag info`, and the required topics were confirmed before running LOG-LIO.

## Run Commands

Terminal A:

```bash
cd /root/slam_ws
source /opt/ros/noetic/setup.bash
source devel/setup.bash
roslaunch log_lio mapping_m2dgr.launch rviz:=false
```

Terminal B:

```bash
cd /root/slam_ws/datasets/M2DGR
source /opt/ros/noetic/setup.bash
rosbag play door_02.bag --topics /velodyne_points /handsfree/imu
```

## Results

Main output files:

| File                                                | Description                       |
| --------------------------------------------------- | --------------------------------- |
| `results/door_02_run1/target_path.txt`              | LOG-LIO trajectory output         |
| `results/door_02_run1/fast_lio_time_log.csv`        | Runtime log                       |
| `results/run_log.csv`                               | Experiment record                 |
| `results/trajectories/m2dgr_door_02_loglio_tum.txt` | Trajectory prepared for evo       |
| `results/trajectories/m2dgr_door_02_gt_tum.txt`     | Converted ground-truth trajectory |

The generated trajectory contains **2469 valid poses**.

## Figures

| Figure                | File                                                |
| --------------------- | --------------------------------------------------- |
| Method pipeline       | `results/figures/loglio_method_pipeline.svg`        |
| Trajectory comparison | `results/figures/door_02_trajectory_comparison.pdf` |
| APE plot              | `results/figures/door_02_ape.pdf`                   |
| RPE plot              | `results/figures/door_02_rpe.pdf`                   |

## Evaluation

Trajectory evaluation was performed with `evo`.

Main evaluation files:

```text
results/error_tables/ape_door_02.txt
results/error_tables/rpe_door_02.txt
results/error_tables/ape_door_02.zip
results/error_tables/rpe_door_02.zip
```

The current evaluation is mainly position-based because the downloaded M2DGR ground-truth text file provides position values but does not include valid orientation quaternions.

Detailed notes:

```text
docs/evaluation_results.md
```

## Runtime Observation

Runtime statistics were extracted from:

```text
results/door_02_run1/fast_lio_time_log.csv
```

For the `door_02` run:

| Metric                              |                Value |
| ----------------------------------- | -------------------: |
| Logged frames                       |                 1268 |
| Average total processing time       |     0.0724 s / frame |
| Average scan size                   | 12043 points / frame |
| Average preprocessing time          |     0.0150 s / frame |
| Average incremental map update time |     0.0116 s / frame |
| Average added map points            |  1022 points / frame |

This confirms that LOG-LIO produced not only a trajectory but also frame-level runtime information during the reproduction.

## Code Reading Map

| Module                      | Main files                                                         |
| --------------------------- | ------------------------------------------------------------------ |
| Main pipeline               | `src/laserMapping.cpp`                                             |
| IMU processing              | `src/IMU_Processing.hpp`                                           |
| Point cloud preprocessing   | `src/preprocess.cpp`, `src/preprocess.h`                           |
| Ring FALS normal estimation | `src/ring_fals/Image_normals.hpp`, `src/ring_fals/range_image.cpp` |
| ikd-tree map                | `include/ikd-Tree/ikd_Tree.cpp`, `include/ikd-Tree/ikd_Tree.h`     |
| Voxel / surfel utility      | `include/voxel_map_util.hpp`                                       |

More details are recorded in:

```text
docs/method_to_code_mapping.md
docs/code_reading_notes.md
```

## Repository Structure

```text
LOG-LIO-Reproduction-and-Analysis/
├── README.md
├── docs/
│   ├── paper_notes.md
│   ├── method_explanation.md
│   ├── method_to_code_mapping.md
│   ├── code_reading_notes.md
│   ├── evaluation_results.md
│   └── runtime_log_analysis.md
├── results/
│   ├── door_02_run1/
│   ├── trajectories/
│   ├── figures/
│   ├── error_tables/
│   └── run_log.csv
├── config_notes/
└── troubleshooting/
```

## Limitations

* Only one M2DGR sequence has been tested so far.
* The downloaded M2DGR door_02 ground-truth file provides valid position values, but its quaternion fields are all zeros. Therefore, this repository reports position-based trajectory evaluation only. Full 6-DoF pose evaluation is left for future work with complete ground-truth orientation data.
* No algorithmic modification is included in this repository.
* A full benchmark across multiple sequences is not yet performed.

## References

* LOG-LIO: A LiDAR-Inertial Odometry with Efficient Local Geometric Information Estimation
* M2DGR: A Multi-modal and Multi-scenario Dataset for Ground Robots
* evo: Python package for trajectory evaluation of odometry and SLAM
