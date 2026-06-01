# Evaluation Results

## Summary

This reproduction evaluates LOG-LIO on two selected M2DGR sequences: `door_02` and `room_01`.

The main quantitative result is based on translation APE/RPE. Rotation APE/RPE is not reported because the frame convention between the M2DGR ground-truth orientation and the LOG-LIO output orientation has not been fully verified.

## Main Results

| Sequence | Setting | Evaluation Scope | APE RMSE (m) | APE Mean (m) | RPE RMSE (m) | RPE Mean (m) |
|---|---|---|---:|---:|---:|---:|
| `room_01` | baseline | translation APE/RPE | 0.249044 | 0.241277 | 0.078890 | 0.064087 |
| `room_01` | no-surfel | translation APE/RPE | 0.246773 | 0.238837 | 0.075243 | 0.059319 |

## Additional Sanity Check

| Sequence | Setting | Evaluation Scope | APE RMSE (m) | APE Mean (m) | Notes |
|---|---|---|---:|---:|---|
| `door_02` | baseline | position-based sanity check | 0.246345 | 0.226276 | Ground-truth quaternion fields are all zeros, so it is not used as a full pose evaluation sequence. |

## Interpretation

The `door_02` sequence was successfully processed and produced a complete LOG-LIO trajectory. However, its downloaded ground-truth file contains valid position values while the quaternion fields are all zeros. Therefore, `door_02` is treated as a successful reproduction run and a position-level sanity check, rather than a full pose evaluation sequence.

The `room_01` sequence is used as the main quantitative evaluation sequence. Its ground-truth file contains non-zero quaternion values, but direct rotation comparison produced unrealistic errors during checking. This suggests that the ground-truth orientation frame and LOG-LIO output pose frame are not directly comparable without further frame-convention verification. Therefore, this project reports translation-based APE/RPE as the reliable quantitative result.

The no-surfel ablation was tested on `room_01` by setting:

- `cloud_surfel: false`
- `point_surfel: false`

The no-surfel result was slightly better than the baseline on this short indoor sequence. The difference is small, so this should not be interpreted as proof that surfel association is unnecessary. A safer conclusion is that the effect of surfel association is scene-dependent.

## Generated Files

Evaluation tables:

- `results/evaluation_summary.csv`
- `results/error_tables/ape_door_02.txt`
- `results/error_tables/rpe_door_02.txt`
- `results/error_tables/ape_room_01.txt`
- `results/error_tables/rpe_room_01.txt`
- `results/error_tables/ape_room_01_no_surfel.txt`
- `results/error_tables/rpe_room_01_no_surfel.txt`

Figures:

- `results/figures/door_02_trajectory_comparison.pdf`
- `results/figures/door_02_ape.pdf`
- `results/figures/door_02_rpe.pdf`
- `results/figures/room_01_trajectory_comparison.pdf`
- `results/figures/room_01_ape.pdf`
- `results/figures/room_01_rpe.pdf`
- `results/figures/room_01_no_surfel_ape.pdf`
- `results/figures/room_01_no_surfel_rpe.pdf`
