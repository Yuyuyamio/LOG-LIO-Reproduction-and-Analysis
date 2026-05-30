# LOG-LIO Code Reading Notes

## Purpose

This document records my current code-level understanding of LOG-LIO. The goal is not to fully rewrite or modify the system, but to locate the main implementation files and connect them with the method-level components of the paper.

## Code Reading Table

| Module | File / Function | What I understood | Remaining question |
|---|---|---|---|
| Main pipeline | src/laserMapping.cpp | This is the central execution file. It loads parameters, subscribes to LiDAR and IMU topics, processes synchronized measurements, updates the map, performs association, publishes odometry, and saves trajectory output. | I still need to understand the full control flow of each iteration in more detail. |
| ROS input | standard_pcl_cbk and imu_cbk in src/laserMapping.cpp | The LiDAR callback receives PointCloud2 messages and the IMU callback receives Imu messages. The messages are stored in buffers and later combined into measurement groups. | I need to inspect how the buffer synchronization handles delayed or missing messages. |
| IMU processing | src/IMU_Processing.hpp | The ImuProcess class handles IMU initialization, forward propagation, extrinsic use, and point cloud undistortion. This is important because a LiDAR scan is captured over a period of time instead of one instant. | I need to better understand the covariance update and the exact undistortion equation. |
| Point cloud preprocessing | src/preprocess.cpp and src/preprocess.h | This module processes raw LiDAR points before mapping. It is connected to LiDAR type selection and normal estimation. For M2DGR, the configuration uses Velodyne-style LiDAR. | I need to compare the preprocessing behavior for Velodyne, Ouster, and Livox modes. |
| Ring FALS normal estimation | src/ring_fals/Image_normals.hpp, src/ring_fals/range_image.cpp, src/ring_fals/range_image.h | These files implement range-image and scan-structure-based normal estimation. The key idea is to use LiDAR ring structure instead of doing expensive unordered neighbor search for every point. | I need to connect the implementation more closely with the Ring FALS equations in the paper. |
| Normal usage | pointNormalBodyToWorld in src/laserMapping.cpp | Normal vectors are transformed from LiDAR/body frame to world frame. These normals are later used during association and normal consistency checking. | I need to inspect how normal uncertainty affects residual construction. |
| Local map | include/ikd-Tree/ikd_Tree.cpp and include/ikd-Tree/ikd_Tree.h | The ikd-tree stores map points and supports incremental insertion, nearest-neighbor search, and deletion of local map regions. | I need to understand the internal update policy of the ikd-tree in more detail. |
| Map update | map_incremental in src/laserMapping.cpp | New points are added into the map after each frame. The code decides which points should be inserted and updates voxel-related information. | I need to inspect how downsampling affects final map density. |
| Local map segmentation | lasermap_fov_segment in src/laserMapping.cpp | The local map is shifted and maintained around the current LiDAR position. Points outside the local region can be removed to keep the map manageable. | I need to check how cube size and detection range affect memory and runtime. |
| Voxel information | include/voxel_map_util.hpp and related usage in src/laserMapping.cpp | Voxel-related information is used to maintain local point distribution and support surfel-level association. | I need to understand how the planarity threshold is selected. |
| Surfel association | cloudSurfel and pointSurfel logic in src/laserMapping.cpp | The code tries to use surfel constraints when local geometric distribution is reliable. This matches the method idea of using richer local surface information. | I need to inspect the exact conditions that decide whether a surfel constraint is accepted. |
| Plane fallback | esti_plane and nearest-neighbor logic in src/laserMapping.cpp | If a reliable surfel constraint is not available, the system can fall back to a point-to-plane style constraint using nearby map points. | I need to compare how often the system uses surfel association versus plane fallback. |
| State update | update_iterated_dyn_share_modified in src/laserMapping.cpp and IKFoM files | The selected geometric residuals are used in an iterated Kalman filter update. This is where data association contributes to pose optimization. | I need to understand the measurement Jacobian construction more deeply. |
| Trajectory output | saveTraj and Log/target_path.txt in src/laserMapping.cpp | The estimated trajectory is saved in TUM-style format as timestamp, position, and quaternion. This file was used for evo evaluation. | I need to verify the exact frame definition of the output trajectory. |
| Runtime log | Log/fast_lio_time_log.csv | The runtime log records per-frame timing and map update information, including total time, incremental time, scan point size, and added points. | I need to compare these runtime values across more sequences. |

## Current Summary

From the current code reading, LOG-LIO can be understood as a pipeline that combines IMU-based motion prediction, LiDAR scan preprocessing, Ring FALS normal estimation, incremental local map maintenance, hierarchical data association, and iterated state estimation.

The most important files for my current reproduction are:

- src/laserMapping.cpp
- src/IMU_Processing.hpp
- src/preprocess.cpp
- src/preprocess.h
- src/ring_fals/Image_normals.hpp
- src/ring_fals/range_image.cpp
- src/ring_fals/range_image.h
- include/ikd-Tree/ikd_Tree.cpp
- include/ikd-Tree/ikd_Tree.h
- include/voxel_map_util.hpp

This code reading confirms that the reproduction is not limited to running a rosbag. It also connects the paper-level method components to the implementation files in the LOG-LIO repository.
