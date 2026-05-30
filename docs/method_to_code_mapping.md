# LOG-LIO Method-to-Code Mapping

## 1. Purpose

This document maps the main LOG-LIO method components to the source code files that implement them. The goal is to connect the algorithm-level understanding with the actual reproduction code.

The current mapping is based on the successfully built and executed LOG-LIO repository, tested on the M2DGR door_02 sequence.

## 2. Main Execution Pipeline

The main execution file is:

src/laserMapping.cpp

This file is the central entry point of the LOG-LIO pipeline. It handles ROS initialization, parameter loading, LiDAR and IMU subscription, mapping, data association, state update, and trajectory output.

Important responsibilities in this file include:

- loading parameters from launch and yaml files
- subscribing to LiDAR and IMU topics
- synchronizing LiDAR and IMU measurements
- transforming point clouds between LiDAR, IMU, and world frames
- maintaining the local map
- performing feature association
- updating the ESKF state
- publishing odometry and path messages
- saving trajectory results to target_path.txt

In this reproduction, the generated executable was:

/root/slam_ws/devel/lib/log_lio/loglio_mapping

## 3. Sensor Input and ROS Topics

The M2DGR configuration uses the following topics:

LiDAR topic:

/velodyne_points

IMU topic:

/handsfree/imu

These topics are defined in:

config/velodyne_m2dgr.yaml

The parameters are loaded in src/laserMapping.cpp through ROS parameter reading. The LiDAR and IMU subscribers are also created in src/laserMapping.cpp.

The relevant callback functions are:

standard_pcl_cbk

imu_cbk

The LiDAR callback receives PointCloud2 messages and stores them in the LiDAR buffer. The IMU callback receives IMU messages and stores them in the IMU buffer. These buffers are later combined into measurement groups for odometry estimation.

## 4. IMU Processing and Point Cloud Undistortion

The IMU processing module is mainly implemented in:

src/IMU_Processing.hpp

This file defines the ImuProcess class. It is responsible for:

- IMU initialization
- gravity and bias handling
- forward propagation
- LiDAR-IMU extrinsic use
- point cloud undistortion using IMU motion

This part is important because LiDAR scans are not captured at one exact instant. During one scan, the platform is moving. IMU data is used to compensate for this motion before scan-to-map registration.

## 5. Point Cloud Preprocessing

Point cloud preprocessing is mainly implemented in:

src/preprocess.cpp

src/preprocess.h

This module handles raw LiDAR point processing before mapping and optimization.

For the M2DGR sequence, the configuration uses Velodyne-style LiDAR processing:

lidar_type: 2

The preprocessing stage is also connected to normal estimation. In this reproduction, the M2DGR launch and yaml configuration enabled Ring FALS normal-related logic.

## 6. Ring FALS Normal Estimation

Ring FALS normal estimation is mainly implemented in:

src/ring_fals/Image_normals.hpp

src/ring_fals/range_image.cpp

src/ring_fals/range_image.h

The purpose of this module is to estimate local surface normals efficiently by using the ring and range-image structure of rotating LiDAR scans.

Instead of treating the point cloud as a completely unordered set, the method uses LiDAR scan organization. This helps reduce repeated nearest-neighbor search for normal estimation.

The relevant parameters are loaded in src/laserMapping.cpp, including:

normal/compute_table

normal/compute_normal

normal/check_normal

normal/ring_table_dir

During initialization, the code calls the normal estimator initialization logic through the preprocessing object. The normal vectors are later used during map association and normal consistency checking.

## 7. ikd-tree Local Map Maintenance

The local map is mainly maintained through the ikd-tree structure.

Important files include:

include/ikd-Tree/ikd_Tree.cpp

include/ikd-Tree/ikd_Tree.h

The main mapping file src/laserMapping.cpp creates and uses:

KD_TREE<PointType> ikdtree

The ikd-tree is used for:

- storing map points
- incremental map update
- nearest-neighbor search
- local map segmentation
- deleting map areas outside the local region
- maintaining voxel-level information

Important related functions and operations include:

lasermap_fov_segment

map_incremental

ikdtree.Build

ikdtree.Add_Points

ikdtree.Delete_Point_Boxes

ikdtree.Nearest_Search

ikdtree.updateVoxelInfo

This part is central to online odometry because the system cannot rebuild the entire map from scratch for every LiDAR frame.

## 8. Voxel and Surfel Information

Voxel and surfel related logic appears in:

src/laserMapping.cpp

include/voxel_map_util.hpp

The code includes parameters such as:

voxel_size

max_layer

layer_point_size

plannar_threshold

max_points_size

max_cov_points_size

surfel_points_min

surfel_points_max

planarity

mid2min

angle_threshold

These parameters describe how local map points are grouped and how local planar or surfel-like structures are judged.

The reproduction log shows that the code searches for terms such as voxel, surfel, plane, nearest, covariance, and planarity in src/laserMapping.cpp. This confirms that data association is not only a simple nearest-neighbor search. It also uses local distribution and normal information.

## 9. Hierarchical Data Association

The association logic is mainly located in src/laserMapping.cpp.

The code first tries to use richer local geometric information when possible. The surfel-related logic includes:

cloudSurfel

pointSurfel

voxel normal

point-to-surfel distance

normal consistency checking

If a valid surfel-type constraint is available, the code can use the surfel normal and point-to-surfel distance. If not, it falls back to local plane estimation using neighboring points.

This matches the method-level understanding:

reliable local distribution -> point-to-surfel style constraint

less reliable local distribution -> point-to-plane style constraint

This hierarchy improves robustness because the system does not force a surfel constraint when local geometry is weak.

## 10. Pose Optimization and State Update

The pose optimization part is connected to the iterated Kalman filter framework.

Important files include:

include/use-ikfom.hpp

include/IKFoM_toolkit/esekfom/esekfom.hpp

src/laserMapping.cpp

The main update call appears in src/laserMapping.cpp through the iterated update logic. The association residuals are used to construct the measurement model, and the ESKF state is updated iteratively.

The estimated state is then used to publish odometry and save trajectory output.

## 11. Trajectory Output

The output trajectory is saved by src/laserMapping.cpp.

The reproduced run generated:

Log/target_path.txt

In the copied result directory, the trajectory is stored as:

results/door_02_run1/target_path.txt

The file follows the format:

timestamp x y z qx qy qz qw

In the M2DGR door_02 run, the trajectory output contained 2469 valid rows. This confirms that the system processed the full rosbag sequence and produced a continuous odometry trajectory.

## 12. What Was Verified in This Reproduction

This reproduction verified the following:

- LOG-LIO can be compiled in a ROS Noetic Docker environment.
- The loglio_mapping executable can be generated.
- The log_lio ROS package can be found by rospack.
- The M2DGR door_02 rosbag contains the required LiDAR and IMU topics.
- The LOG-LIO M2DGR launch file can start successfully.
- The system can process the full door_02 sequence.
- The system generates trajectory output in target_path.txt.
- The source code structure matches the expected method components: Ring FALS normal estimation, voxel/ikd-tree map maintenance, hierarchical association, and pose optimization.

## 13. Current Understanding

LOG-LIO is not only a direct scan-to-map registration system. Its main design is to improve how local geometry is estimated, maintained, and used during association.

The pipeline can be understood as:

LiDAR and IMU input

point cloud preprocessing and IMU undistortion

Ring FALS normal estimation

local map maintenance with ikd-tree and voxel information

surfel or plane association depending on local geometry reliability

iterated state update

trajectory output

This mapping helps turn the reproduction from only running the code into understanding how the method is implemented in the repository.
