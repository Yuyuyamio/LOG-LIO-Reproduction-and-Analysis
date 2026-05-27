# LOG-LIO Pipeline Draft

## Text Version

```text
Raw LiDAR Scan + IMU
        ↓
IMU Preintegration / Motion Prediction
        ↓
Scan Undistortion
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