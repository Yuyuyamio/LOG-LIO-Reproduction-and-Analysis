# LOG-LIO Reproduction and Analysis

This repository documents my reproduction and analysis of **LOG-LIO**, a LiDAR-Inertial Odometry system that uses local geometric information for scan-to-map registration and pose estimation.

The goal of this project is not to propose a new SLAM algorithm. Instead, it focuses on understanding how LOG-LIO connects **normal estimation**, **voxel-level point distribution**, **hierarchical data association**, and **pose optimization** in a working LiDAR-inertial odometry pipeline.

> This repository is a reproduction-oriented project. It does not vendor the full official LOG-LIO source code. The official code was cloned and built locally in a Docker/ROS workspace, while this repository records the reproduction notes, configuration notes, scripts, results, figures, troubleshooting records, and report materials.

---

## 1. Current Status

A complete first reproduction run has been finished on the **M2DGR `door_02`** sequence.

Completed items:

- Built LOG-LIO successfully in a ROS Noetic Docker environment.
- Fixed ROS / PCL / OpenCV build issues and documented them.
- Verified the M2DGR `door_02.bag` topics:
  - `/velodyne_points`
  - `/handsfree/imu`
- Ran LOG-LIO on the full `door_02` sequence.
- Generated a trajectory output file with 2469 valid rows.
- Created trajectory sanity checks and trajectory visualization files.
- Performed evo-based APE / RPE evaluation.
- Analyzed runtime logs from `fast_lio_time_log.csv`.
- Mapped the main LOG-LIO method components to source-code locations.

---

## 2. Repository Structure

```text
LOG-LIO-Reproduction-and-Analysis/
├── README.md
├── config_notes/
│   ├── environment.md
│   └── phase2_ubuntu_commands.md
├── docs/
│   ├── paper_notes.md
│   ├── method_explanation.md
│   ├── method_to_code_mapping.md
│   ├── code_reading_notes.md
│   ├── door_02_run_notes.md
│   ├── door_02_result_analysis.md
│   ├── trajectory_visualization_notes.md
│   ├── runtime_log_analysis.md
│   ├── evaluation_results.md
│   └── reproduction_report.md
├── results/
│   ├── door_02_run1/
│   ├── trajectories/
│   ├── figures/
│   ├── error_tables/
│   └── run_log.csv
└── troubleshooting/
    └── ros_build_errors.md
```

Large datasets such as `.bag` files are not included in this repository.

---

## 3. Method Summary

LOG-LIO can be understood as the following pipeline:

```text
Raw LiDAR Scan + IMU
        ↓
IMU Processing / Scan Undistortion
        ↓
Ring FALS Normal Estimation
        ↓
Voxel Map / Extended ikd-tree
        ↓
Point Distribution Update
        ↓
Hierarchical Data Association
(point-to-surfel → point-to-plane)
        ↓
Pose Optimization
        ↓
Updated Odometry + Local Map
```

The main method components studied in this project are:

- **Ring FALS normal estimation**: estimates local surface normals using LiDAR scan ring and range-image structure.
- **Voxel map / extended ikd-tree**: maintains local map information and voxel-level point distribution incrementally.
- **Hierarchical data association**: prioritizes point-to-surfel association when local geometry is reliable and falls back to point-to-plane association when needed.

More detailed notes are available in:

- `docs/paper_notes.md`
- `docs/method_explanation.md`
- `docs/method_to_code_mapping.md`
- `docs/code_reading_notes.md`

---

## 4. Environment

The reproduction was carried out using:

- WSL2 Ubuntu
- Docker
- ROS Noetic
- catkin workspace
- PCL
- Eigen
- OpenCV
- evo for trajectory evaluation

The final compiled executable was generated inside the Docker workspace:

```text
/root/slam_ws/devel/lib/log_lio/loglio_mapping
```

Environment and build notes are recorded in:

- `config_notes/environment.md`
- `config_notes/phase2_ubuntu_commands.md`
- `troubleshooting/ros_build_errors.md`

---

## 5. Dataset

The first reproduction run uses the M2DGR **`door_02`** sequence.

Rosbag information:

```text
Sequence: door_02
Duration: about 127 s
Size: about 9.8 GB
LiDAR topic: /velodyne_points
IMU topic: /handsfree/imu
```

The full M2DGR dataset is large, so this repository only documents selected sequence experiments instead of storing the original rosbag files.

---

## 6. How to Run

Inside the ROS Noetic Docker container:

```bash
cd /root/slam_ws
source /opt/ros/noetic/setup.bash
source devel/setup.bash
roslaunch log_lio mapping_m2dgr.launch rviz:=false
```

In another terminal attached to the same container:

```bash
cd /root/slam_ws/datasets/M2DGR
source /opt/ros/noetic/setup.bash
rosbag play door_02.bag --topics /velodyne_points /handsfree/imu
```

The main trajectory output is saved as:

```text
Log/target_path.txt
```

The copied reproduction result is stored in:

```text
results/door_02_run1/target_path.txt
```

---

## 7. Results

### 7.1 Trajectory Output

The first successful run generated:

```text
results/door_02_run1/target_path.txt
```

The trajectory contains **2469 valid rows** in TUM-style format:

```text
timestamp x y z qx qy qz qw
```

### 7.2 Runtime Observation

The runtime log is stored in:

```text
results/door_02_run1/fast_lio_time_log.csv
```

Summary from the current run:

```text
Logged frames: 1268
Average total processing time per frame: about 0.0724 s
Average scan point size: about 12043 points
Average preprocess time: about 0.0150 s
Average incremental map update time: about 0.0116 s
Average added map points per frame: about 1022 points
```

### 7.3 Evaluation Files

The evo-based evaluation files are stored in:

```text
results/error_tables/
```

Important files:

- `ape_door_02.txt`
- `rpe_door_02.txt`
- `ape_door_02.zip`
- `rpe_door_02.zip`

The evaluation notes are in:

```text
docs/evaluation_results.md
```

The current ground-truth text file provides position values but does not contain valid orientation quaternions. Therefore, the current APE / RPE evaluation should be interpreted mainly as a **position-based trajectory evaluation**.

---

## 8. Figures

Generated figures include:

- `results/figures/door_02_trajectory_comparison.pdf`
- `results/figures/door_02_ape.pdf`
- `results/figures/door_02_rpe.pdf`
- `results/figures/loglio_method_pipeline.svg`
- `results/door_02_run1/trajectory_xy.svg`
- `results/door_02_run1/trajectory_z_time.svg`

The method pipeline figure summarizes the connection between LiDAR/IMU input, Ring FALS normal estimation, voxel map maintenance, hierarchical association, and pose optimization.

---

## 9. Troubleshooting

The reproduction involved several practical ROS and build issues, including missing ROS packages and OpenCV linking problems. These were recorded in:

- `troubleshooting.md`
- `troubleshooting/ros_build_errors.md`

This is included intentionally because reproducing a SLAM system is not only about running a final command. The build and dataset issues are part of the engineering process.

---

## 10. Limitations and Next Steps

Current limitations:

- Only one M2DGR sequence has been fully processed so far.
- The current ground-truth orientation is not valid, so evaluation mainly focuses on position error.
- No algorithmic modification has been made.
- No comparison with FAST-LIO2 or other baselines has been completed yet.

Possible next steps:

- Run a second M2DGR sequence.
- Add a clearer failure or drift analysis case.
- Improve the reproduction report into a polished PDF.
- Compare LOG-LIO with another LIO baseline or published reference result.
- Inspect the Ring FALS and surfel association implementation in more detail.

---

## 11. References

- LOG-LIO official repository: https://github.com/tiev-tongji/LOG-LIO
- LOG-LIO paper: https://arxiv.org/abs/2307.09531
- M2DGR dataset: https://github.com/SJTU-ViSYS/M2DGR
- evo trajectory evaluation tool: https://github.com/MichaelGrupp/evo
