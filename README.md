# LOG-LIO Reproduction and Analysis

This repository documents a reproduction and analysis of **LOG-LIO**, a LiDAR-Inertial Odometry system based on efficient local geometric information estimation.

The goal of this project is not to modify the original algorithm. Instead, it focuses on building LOG-LIO, running it on selected M2DGR sequences, evaluating the trajectory outputs, and connecting the paper-level method with source-code modules.

## What This Repository Contains

* ROS Noetic Docker-based reproduction notes.
* M2DGR `door_02` and `room_01` experiment results.
* LOG-LIO trajectory outputs in TUM format.
* Translation-based APE/RPE evaluation using evo.
* Runtime statistics from `fast_lio_time_log.csv`.
* A small no-surfel ablation on `room_01`.
* RViz screenshots for local map and trajectory visualization.
* Method-to-code mapping for Ring FALS, voxel map maintenance, and hierarchical data association.

## Method Focus

The reproduced LOG-LIO pipeline can be summarized as:

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
    ↓
Pose optimization
    ↓
Odometry trajectory
```

The main method components studied in this project are:

| Component                   | Purpose                                                      |
| --------------------------- | ------------------------------------------------------------ |
| Ring FALS normal estimation | Efficient local normal estimation using LiDAR scan structure |
| Voxel / ikd-tree map        | Incremental local map and point distribution maintenance     |
| Hierarchical association    | Point-to-surfel association with point-to-plane fallback     |
| State update                | Uses geometric residuals for pose optimization               |

## Reproduction Setup

| Item            | Setting               |
| --------------- | --------------------- |
| Host            | Windows + WSL2 Ubuntu |
| Runtime         | Docker container      |
| ROS             | Noetic                |
| Build system    | catkin                |
| Dataset         | M2DGR                 |
| Evaluation tool | evo                   |

The original LOG-LIO source code is not redistributed in this repository. It was cloned and built locally inside the ROS Noetic Docker workspace.

## Dataset and Runs

| Sequence  | Setting   | Trajectory rows | Status  |
| --------- | --------- | --------------: | ------- |
| `door_02` | baseline  |            2469 | success |
| `room_01` | baseline  |             722 | success |
| `room_01` | no-surfel |             723 | success |

Required M2DGR topics:

```text
/velodyne_points
/handsfree/imu
```

Main LOG-LIO launch command:

```bash
roslaunch log_lio mapping_m2dgr.launch rviz:=false
```

Rosbag playback command:

```bash
rosbag play <sequence>.bag --topics /velodyne_points /handsfree/imu
```

## Evaluation Results

The main quantitative result is translation-based APE/RPE evaluation.

| Sequence  | Setting   | Evaluation scope                         | APE RMSE (m) | APE Mean (m) |            RPE RMSE (m) |            RPE Mean (m) |
| --------- | --------- | ---------------------------------------- | -----------: | -----------: | ----------------------: | ----------------------: |
| `room_01` | baseline  | valid GT quaternion, translation metrics |     0.249044 |     0.241277 |                0.078890 |                0.064087 |
| `room_01` | no-surfel | valid GT quaternion, translation metrics |     0.246773 |     0.238837 |                0.075243 |                0.059319 |
| `door_02` | baseline  | position-based sanity check              |     0.246345 |     0.226276 | not used as main metric | not used as main metric |

`door_02` is treated as a position-based sanity check because the downloaded ground-truth file contains valid position values but invalid quaternion fields.

`room_01` is used as the main quantitative sequence. Its ground-truth file contains non-zero quaternion values, but rotation APE/RPE is not reported because the frame convention between the M2DGR ground-truth orientation and LOG-LIO output orientation has not been fully verified.

## Ablation Result

A small no-surfel ablation was tested on `room_01`.

| Setting   | `cloud_surfel` | `point_surfel` | APE RMSE (m) | RPE RMSE (m) |
| --------- | -------------- | -------------- | -----------: | -----------: |
| baseline  | true           | true           |     0.249044 |     0.078890 |
| no-surfel | false          | false          |     0.246773 |     0.075243 |

On this short indoor sequence, disabling surfel association did not degrade the translation result. The difference is small, so this should not be interpreted as proof that surfel association is unnecessary. A safer conclusion is that the effect of surfel association is scene-dependent.

## Figures and Result Files

| Type                       | Path                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------- |
| Evaluation summary         | `results/evaluation_summary.csv`                                                   |
| Run log                    | `results/run_log.csv`                                                              |
| Method pipeline            | `results/figures/loglio_method_pipeline.svg`                                       |
| RViz map screenshots       | `results/figures/room_01_rviz_map_1.png`, `results/figures/room_01_rviz_map_2.png` |
| Trajectory and error plots | `results/figures/`                                                                 |
| APE/RPE outputs            | `results/error_tables/`                                                            |
| TUM trajectories           | `results/trajectories/`                                                            |
| Runtime logs               | `results/door_02_run1/`, `results/room_01_run1/`, `results/room_01_no_surfel/`     |

## Scripts

| Script                       | Purpose                                              |
| ---------------------------- | ---------------------------------------------------- |
| `scripts/run_m2dgr.sh`       | Documents the two-terminal LOG-LIO running procedure |
| `scripts/evaluate_ape.sh`    | Runs evo APE evaluation                              |
| `scripts/evaluate_rpe.sh`    | Runs evo RPE evaluation                              |
| `scripts/collect_runtime.py` | Extracts runtime statistics                          |
| `scripts/plot_trajectory.py` | Generates a simple XY trajectory plot                |

## Notes and Limitations

* Large `.bag` files are excluded from this repository.
* The original LOG-LIO source code is not redistributed here.
* `door_02` is not used as a full pose evaluation sequence because its quaternion fields are invalid.
* Rotation APE/RPE is not reported because the ground-truth orientation frame and LOG-LIO output frame require further verification.
* The no-surfel experiment is a small ablation on one indoor sequence only.
* FAST-LIO / FAST-LIO2 comparison was investigated but not included as a final result.

## Main Documentation

| File                                  | Purpose                                   |
| ------------------------------------- | ----------------------------------------- |
| `docs/paper_notes.md`                 | Paper understanding notes                 |
| `docs/method_explanation.md`          | Method explanation                        |
| `docs/method_to_code_mapping.md`      | Mapping from method modules to code files |
| `docs/code_reading_notes.md`          | Code reading notes                        |
| `docs/evaluation_results.md`          | Evaluation result explanation             |
| `docs/failure_analysis.md`            | Drift / short-term error discussion       |
| `docs/rotation_evaluation_notes.md`   | Rotation evaluation limitation            |
| `docs/visualization_notes.md`         | RViz visualization notes                  |
| `config_notes/parameter_notes.md`     | No-surfel ablation notes                  |
| `troubleshooting/ros_build_errors.md` | Build troubleshooting record              |
