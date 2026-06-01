# LOG-LIO Method-to-Code Mapping

## Purpose

This document connects the main LOG-LIO method components with the source-code modules inspected during the reproduction. It is based on the LOG-LIO code that was successfully built and executed on the M2DGR `door_02` and `room_01` sequences.

## Main Pipeline

| Method component | Main code location | Role in the running system |
|---|---|---|
| Main mapping pipeline | `src/laserMapping.cpp` | Loads parameters, subscribes to LiDAR/IMU topics, manages scan-to-map registration, updates the state, publishes odometry, and saves trajectory output. |
| M2DGR launch entry | `launch/mapping_m2dgr.launch` | Starts the LOG-LIO pipeline with the M2DGR configuration. |
| M2DGR configuration | `config/velodyne_m2dgr.yaml` | Defines the Velodyne LiDAR topic, Handsfree IMU topic, LiDAR type, scan line, extrinsic parameters, normal estimation options, and surfel association options. |
| IMU processing | `src/IMU_Processing.hpp` | Performs IMU initialization, motion propagation, gravity/bias handling, and scan undistortion. |
| Point cloud preprocessing | `src/preprocess.cpp`, `src/preprocess.h` | Handles LiDAR-specific preprocessing before registration and mapping. |
| Ring FALS normal estimation | `src/ring_fals/Image_normals.hpp`, `src/ring_fals/range_image.cpp`, `src/ring_fals/range_image.h` | Estimates local surface normals by using LiDAR ring and range-image structure. |
| Local map maintenance | `include/ikd-Tree/ikd_Tree.cpp`, `include/ikd-Tree/ikd_Tree.h` | Supports incremental map insertion, deletion, and nearest-neighbor query. |
| Voxel / surfel information | `include/voxel_map_util.hpp`, `src/laserMapping.cpp` | Maintains local geometric distribution information used for surfel or plane association. |
| Hierarchical data association | `src/laserMapping.cpp` | Uses surfel-related constraints when available and falls back to plane-style constraints when local geometry is less reliable. |
| State update | `include/use-ikfom.hpp`, `include/IKFoM_toolkit/esekfom/esekfom.hpp`, `src/laserMapping.cpp` | Uses geometric residuals in an iterated filtering framework to update the estimated state. |
| Trajectory output | `src/laserMapping.cpp`, `Log/target_path.txt` | Saves the estimated odometry trajectory in TUM-style format for later evo evaluation. |

## Input Topics Used in This Reproduction

The M2DGR experiments used the following topics:

```text
/velodyne_points
/handsfree/imu
```

These topics were confirmed in the M2DGR rosbags before running LOG-LIO. The same topic setting is recorded in `config_notes/m2dgr_config_notes.md`.

## How the Paper Method Appears in Code

### Ring FALS normal estimation

At the method level, Ring FALS uses the organized structure of rotating LiDAR scans to estimate local normals efficiently. In code, this part is mainly connected to the `src/ring_fals/` directory and the preprocessing pipeline. The relevant parameters include normal computation and checking options in the M2DGR YAML configuration.

### Voxel map and ikd-tree

The local map is not rebuilt from scratch for each scan. LOG-LIO uses ikd-tree-related code for incremental local map maintenance and nearest-neighbor search. Voxel-level information is also used to describe local point distribution and support association decisions.

### Hierarchical association

The method description says that LOG-LIO uses hierarchical data association, with point-to-surfel constraints when local distribution information is reliable and fallback constraints when it is not. In the code, this logic is mainly tied to `src/laserMapping.cpp` and surfel-related options such as:

```text
cloud_surfel
point_surfel
```

This connection was also tested experimentally through the `room_01` no-surfel ablation, where both options were disabled.

## Reproduction Evidence

The code path above was verified through the following reproduction outputs:

| Evidence | File or result |
|---|---|
| Successful LOG-LIO build | `troubleshooting/ros_build_errors.md` |
| Successful M2DGR runs | `results/run_log.csv` |
| Trajectory outputs | `results/door_02_run1/target_path.txt`, `results/room_01_run1/target_path.txt` |
| Evaluation results | `results/evaluation_summary.csv`, `docs/evaluation_results.md` |
| Runtime analysis | `results/door_02_run1/fast_lio_time_log.csv`, `results/room_01_run1/fast_lio_time_log.csv` |
| No-surfel ablation | `config_notes/parameter_notes.md`, `results/room_01_no_surfel/` |

## Current Understanding

LOG-LIO is not just a direct scan-to-map registration pipeline. Its main design is to improve how local geometric information is estimated, maintained, and used during data association. The code structure reflects this through Ring FALS normal estimation, voxel/ikd-tree map maintenance, surfel-related association logic, and iterated state update.

The reproduction therefore goes beyond simply running a rosbag: it links the paper's method claims to specific source-code modules and verifies the resulting pipeline on real M2DGR sequences.

## Remaining Questions

- The exact frame convention between M2DGR ground-truth orientation and LOG-LIO output orientation still needs further verification.
- The surfel association thresholds need deeper inspection before making strong claims about their behavior across different scenes.
- More sequences would be needed to generalize the no-surfel ablation result beyond `room_01`.
