# LOG-LIO Pipeline Draft

## 1. Text Version

Raw LiDAR Scan + IMU
        |
        v
IMU Preintegration / Motion Prediction
        |
        v
Scan Undistortion
        |
        v
Ring FALS Normal Estimation
        |
        v
Voxel Map / Extended ikd-tree
        |
        v
Point Distribution Update
        |
        v
Hierarchical Data Association
(point-to-surfel -> point-to-plane)
        |
        v
Pose Optimization
        |
        v
Updated Odometry + Local Map

---

## 2. Mermaid Draft

flowchart TD
    A[Raw LiDAR Scan + IMU] --> B[IMU Preintegration / Motion Prediction]
    B --> C[Scan Undistortion]
    C --> D[Ring FALS Normal Estimation]
    D --> E[Voxel Map / Extended ikd-tree]
    E --> F[Point Distribution Update]
    F --> G[Hierarchical Data Association]
    G --> H[Point-to-surfel Association]
    G --> I[Point-to-plane Fallback]
    H --> J[Pose Optimization]
    I --> J
    J --> K[Updated Odometry + Local Map]

---

## 3. Why this pipeline matters

This pipeline shows that LOG-LIO is not only a LiDAR-IMU fusion system. Its key feature is the use of local geometric information.

The important logic is:

normal estimation -> point distribution -> data association -> pose optimization

This path explains why local geometry affects the final odometry result.

---

## 4. Notes for Final Figure

The final pipeline figure should be clean and simple. It should not be only an RViz screenshot. It should clearly show how raw LiDAR and IMU data are processed, how local geometry is estimated, and how this information supports pose optimization.

The most important part to highlight is:

Ring FALS normal estimation
        |
        v
Voxel-level point distribution
        |
        v
Hierarchical association
        |
        v
Pose optimization
