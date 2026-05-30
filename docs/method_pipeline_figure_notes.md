# LOG-LIO Method Pipeline Figure Notes

## Purpose

This figure summarizes the main LOG-LIO pipeline from raw LiDAR and IMU input to odometry output.

The goal of the figure is to explain how LOG-LIO uses local geometric information in the LiDAR-inertial odometry process.

## Figure File

results/figures/loglio_method_pipeline.svg

## Pipeline Explanation

The pipeline starts from raw LiDAR and IMU data. IMU processing provides motion prediction and helps undistort the LiDAR scan.

After preprocessing, LOG-LIO applies Ring FALS normal estimation. This step uses the LiDAR scan ring structure and range-image information to estimate local surface normals efficiently.

The system then maintains a voxel map using an extended ikd-tree structure. Each voxel stores local point distribution information, which helps judge whether the local geometry is reliable.

During data association, LOG-LIO uses a hierarchical strategy. If the local geometric distribution is reliable, point-to-surfel association can be used. If it is not reliable, the system falls back to point-to-plane association.

Finally, the selected geometric constraints are used in pose optimization, producing updated odometry and an updated local map.
