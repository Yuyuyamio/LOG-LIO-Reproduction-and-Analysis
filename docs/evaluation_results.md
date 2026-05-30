# Evaluation Results: M2DGR door_02

## 1. Purpose

This document records the trajectory evaluation result of LOG-LIO on the M2DGR `door_02` sequence.

The evaluation was performed using `evo`.

## 2. Trajectories

Estimated trajectory:

results/trajectories/m2dgr_door_02_loglio_tum.txt

Ground truth trajectory:

results/trajectories/m2dgr_door_02_gt_tum.txt

The ground truth file provides timestamp and position. Since its orientation columns are zero, a unit quaternion was used during conversion:

0 0 0 1

Therefore, the current evaluation should be interpreted mainly as a position-based trajectory evaluation.

## 3. Evaluation Commands

APE / ATE command:

evo_ape tum results/trajectories/m2dgr_door_02_gt_tum.txt results/trajectories/m2dgr_door_02_loglio_tum.txt -a

RPE command:

evo_rpe tum results/trajectories/m2dgr_door_02_gt_tum.txt results/trajectories/m2dgr_door_02_loglio_tum.txt -a

## 4. Result Summary

| Sequence | ATE RMSE / APE RMSE | ATE Mean / APE Mean | RPE RMSE | RPE Mean | Status |
|---|---:|---:|---:|---:|---|
| M2DGR door_02 | 0.246345 m | 0.226276 m | 0.365113 m | 0.218278 m | Success |

## 5. Generated Figures

The following figures were generated:

- results/figures/door_02_trajectory_comparison.pdf
- results/figures/door_02_ape.pdf
- results/figures/door_02_rpe.pdf

## 6. Interpretation

The APE result measures the global position error after alignment. It is useful for checking the overall difference between the reproduced LOG-LIO trajectory and the reference trajectory.

The RPE result measures relative motion error. It is useful for checking local drift between nearby trajectory segments.

At this stage, the result should be treated as a reproduction-oriented evaluation rather than a full benchmark. The main purpose is to prove that the reproduced system can process a real M2DGR sequence, generate a trajectory, and be evaluated with standard SLAM evaluation tools.

## 7. Limitation

The M2DGR door_02 ground truth text file used here contains position values but no valid orientation quaternion. Because of this, the current evaluation focuses on position consistency. A more complete evaluation would require a ground truth file with valid orientation or an official benchmark-format trajectory.
