# LOG-LIO Reproduction and Analysis

This repository documents my reproduction and analysis of LOG-LIO, a LiDAR-Inertial Odometry system with efficient local geometric information estimation.

## Repository Strategy

This repository is organized as a reproduction-oriented project rather than a direct fork of the official LOG-LIO repository. The official LOG-LIO code will be cloned locally for building and testing, while this repository mainly records my reproduction notes, environment setup, scripts, results, figures, and final report.

The goal of this project is not to propose a new SLAM algorithm, but to understand how LOG-LIO uses local geometric information, including normal estimation, point distribution, and hierarchical data association, to improve LiDAR-inertial odometry.

## Project Goals

- Understand the core method of LOG-LIO
- Reproduce LOG-LIO on selected M2DGR sequences
- Evaluate the reproduced trajectory using ATE and RPE
- Analyze successful and failed cases
- Document ROS, dataset, and evaluation issues

## Current Stage

This repository is currently in the early reproduction stage. I first organize the paper understanding, project structure, and experimental plan before running the full SLAM system.

## Planned Outputs

- Paper notes
- Method explanation
- Reproduction scripts
- M2DGR experiment results
- Trajectory comparison figures
- ATE / RPE evaluation results
- Troubleshooting records
- Final reproduction report