# Code Reading Notes

## Purpose

This file records the main source-code modules inspected during the LOG-LIO reproduction. The goal is to connect the paper-level method with the actual implementation, rather than fully rewrite the system.

## Main Code Map

| Module | Main file / location | What I checked | Understanding |
|---|---|---|---|
| Main pipeline | `src/laserMapping.cpp` | ROS initialization, topic subscription, mapping loop, trajectory saving | This is the central file that connects LiDAR/IMU input, mapping, state update, and trajectory output generation. |
| M2DGR launch | `launch/mapping_m2dgr.launch` | Launch entry used for M2DGR experiments | This launch file starts LOG-LIO on the selected M2DGR sequences. |
| M2DGR config | `config/velodyne_m2dgr.yaml` | LiDAR topic, IMU topic, scan line, extrinsic parameters, surfel flags | This config controls the Velodyne-based M2DGR reproduction setup. |
| IMU processing | `src/IMU_Processing.hpp` | IMU initialization, motion propagation, scan undistortion | IMU data is used to predict motion between LiDAR scans and compensate scan distortion. |
| Point cloud preprocessing | `src/preprocess.cpp`, `src/preprocess.h` | LiDAR type handling and raw point filtering | This module prepares raw LiDAR points before normal estimation and mapping. |
| Ring FALS normal estimation | `src/ring_fals/` | Range-image and ring-structure normal estimation | LOG-LIO uses LiDAR scan structure to estimate local normals more efficiently than unordered neighbor search. |
| Local map maintenance | `include/ikd-Tree/` | Incremental map insertion and nearest-neighbor structure | The ikd-tree supports incremental local map update and nearest-neighbor query. |
| Voxel / surfel information | `include/voxel_map_util.hpp` | Voxel-level distribution and surfel-related utilities | Voxel information helps judge local geometric reliability for data association. |
| Data association | `src/laserMapping.cpp` | Point-to-surfel and point-to-plane related logic | LOG-LIO uses hierarchical association: surfel constraints when available, fallback constraints otherwise. |
| Output trajectory | `src/laserMapping.cpp`, `Log/target_path.txt` | TUM-style trajectory output | The generated trajectory is saved and later used for evo evaluation. |

## Notes from Reproduction

The most important implementation file for understanding the running system is `src/laserMapping.cpp`. It connects parameter loading, ROS topics, scan processing, local map update, state estimation, and trajectory output.

The most important configuration file for this reproduction is `config/velodyne_m2dgr.yaml`, because the M2DGR runs use the following topics:

```text
/velodyne_points
/handsfree/imu
```

The no-surfel ablation was performed by changing:

```text
cloud_surfel: false
point_surfel: false
```

This was used to test whether surfel-based association clearly improved the result on the `room_01` sequence.

## Remaining Questions

- The exact frame convention between M2DGR ground-truth orientation and LOG-LIO output orientation still needs further verification.
- The internal thresholds for accepting surfel constraints need deeper code inspection.
- More sequences would be needed before making a strong conclusion about the effect of surfel association.
