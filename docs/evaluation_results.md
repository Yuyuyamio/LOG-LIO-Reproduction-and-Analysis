# Evaluation Results

## Summary

This reproduction evaluates LOG-LIO on two M2DGR sequences: `door_02` and `room_01`.

| Sequence | Setting   | Evaluation Scope    | APE RMSE (m) | APE Mean (m) | RPE RMSE (m) | RPE Mean (m) |
| -------- | --------- | ------------------- | -----------: | -----------: | -----------: | -----------: |
| door_02  | baseline  | position-based      |     0.246345 |     0.226276 |     0.365113 |     0.218278 |
| room_01  | baseline  | valid GT quaternion |     0.249044 |     0.241277 |     0.078890 |     0.064087 |
| room_01  | no-surfel | valid GT quaternion |     0.246773 |     0.238837 |     0.075243 |     0.059319 |

## Interpretation

The `door_02` sequence was successfully processed, but its downloaded ground-truth file contains valid position values while the quaternion fields are all zeros. Therefore, the `door_02` result is treated as a position-based trajectory evaluation.

The `room_01` sequence provides valid ground-truth quaternion values, so it is more suitable as the main quantitative evaluation sequence. On `room_01`, the baseline run achieved an APE RMSE of 0.249044 m and an RPE RMSE of 0.078890 m.

A small no-surfel ablation was also tested on `room_01` by setting:

* `cloud_surfel: false`
* `point_surfel: false`

The no-surfel result was slightly better than the baseline on this short indoor sequence. The difference is small, so this should not be interpreted as proof that surfel association is unnecessary. A safer conclusion is that the effect of surfel association is scene-dependent.

## Generated Files

Evaluation tables:

* `results/evaluation_summary.csv`
* `results/error_tables/ape_door_02.txt`
* `results/error_tables/rpe_door_02.txt`
* `results/error_tables/ape_room_01.txt`
* `results/error_tables/rpe_room_01.txt`
* `results/error_tables/ape_room_01_no_surfel.txt`
* `results/error_tables/rpe_room_01_no_surfel.txt`

Figures:

* `results/figures/door_02_trajectory_comparison.pdf`
* `results/figures/door_02_ape.pdf`
* `results/figures/door_02_rpe.pdf`
* `results/figures/room_01_trajectory_comparison.pdf`
* `results/figures/room_01_ape.pdf`
* `results/figures/room_01_rpe.pdf`
* `results/figures/room_01_no_surfel_ape.pdf`
* `results/figures/room_01_no_surfel_rpe.pdf`
