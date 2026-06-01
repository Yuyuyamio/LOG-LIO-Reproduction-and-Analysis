# LOG-LIO Reproduction and Analysis

This repository documents a reproduction and analysis of **LOG-LIO**, a LiDAR-Inertial Odometry system based on efficient local geometric information estimation.

The goal is not to modify the original algorithm. The focus is to build LOG-LIO, run it on M2DGR sequences, evaluate the output trajectories, and connect the paper-level method with the source code.

## What is included

- ROS Noetic Docker reproduction notes
- M2DGR `door_02` and `room_01` experiment results
- LOG-LIO trajectory outputs in TUM format
- evo APE/RPE evaluation results
- Runtime statistics from `fast_lio_time_log.csv`
- A small no-surfel ablation on `room_01`
- Method-to-code mapping for Ring FALS, voxel map maintenance, and hierarchical association

## Method focus

LOG-LIO uses local geometric information to support scan-to-map registration and state estimation.

```text
LiDAR + IMU
   ↓
IMU processing and scan undistortion
   ↓
Ring FALS normal estimation
   ↓
Voxel map / extended ikd-tree maintenance
   ↓
Hierarchical data association
   ↓
Pose optimization
   ↓
Odometry trajectory
```

The main components studied here are:

| Component | Purpose |
|---|---|
| Ring FALS normal estimation | Efficient local normal estimation using LiDAR scan structure |
| Voxel / ikd-tree map | Incremental local map and point distribution maintenance |
| Hierarchical association | Point-to-surfel association with point-to-plane fallback |
| State update | Uses geometric residuals for pose optimization |

## Reproduction setup

| Item | Setting |
|---|---|
| Host | Windows + WSL2 Ubuntu |
| Runtime | Docker container |
| ROS | Noetic |
| Build system | catkin |
| Dataset | M2DGR |
| Evaluation | evo |

The LOG-LIO source code is not copied into this repository. It was cloned and built locally inside the ROS Noetic Docker workspace.

## Dataset and runs

| Sequence | Setting | Trajectory rows | Status |
|---|---|---:|---|
| `door_02` | baseline | 2469 | success |
| `room_01` | baseline | 722 | success |
| `room_01` | no-surfel | 723 | success |

Required topics:

```text
/velodyne_points
/handsfree/imu
```

Main run command:

```bash
roslaunch log_lio mapping_m2dgr.launch rviz:=false
```

Rosbag playback:

```bash
rosbag play <sequence>.bag --topics /velodyne_points /handsfree/imu
```

## Evaluation results

| Sequence | Setting | Evaluation scope | APE RMSE (m) | RPE RMSE (m) |
|---|---|---|---:|---:|
| `door_02` | baseline | position-based | 0.246345 | 0.365113 |
| `room_01` | baseline | valid GT quaternion | 0.249044 | 0.078890 |
| `room_01` | no-surfel | valid GT quaternion | 0.246773 | 0.075243 |

`door_02` is treated as position-based because the downloaded ground-truth file provides valid position values but zero quaternion fields. `room_01` provides valid quaternion values and is used as the main quantitative sequence.

## Figures and results

| Type | Path |
|---|---|
| Evaluation summary | `results/evaluation_summary.csv` |
| Run log | `results/run_log.csv` |
| Method pipeline | `results/figures/loglio_method_pipeline.svg` |
| Trajectory and error plots | `results/figures/` |
| APE/RPE outputs | `results/error_tables/` |
| TUM trajectories | `results/trajectories/` |
| Runtime logs | `results/door_02_run1/`, `results/room_01_run1/` |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/run_m2dgr.sh` | Documents the two-terminal LOG-LIO running procedure |
| `scripts/evaluate_ape.sh` | Runs evo APE evaluation |
| `scripts/evaluate_rpe.sh` | Runs evo RPE evaluation |
| `scripts/collect_runtime.py` | Extracts runtime statistics |
| `scripts/plot_trajectory.py` | Generates a simple XY trajectory plot |

## Notes

- Large `.bag` files are excluded from this repository.
- `door_02` evaluation is position-based due to invalid GT quaternion fields.
- The no-surfel experiment is a small ablation on one indoor sequence only; it should not be treated as a general conclusion about LOG-LIO.
- No original LOG-LIO source code is redistributed here.

## References

- LOG-LIO: https://github.com/tiev-tongji/LOG-LIO
- M2DGR: https://github.com/SJTU-ViSYS/M2DGR
- evo: https://github.com/MichaelGrupp/evo
