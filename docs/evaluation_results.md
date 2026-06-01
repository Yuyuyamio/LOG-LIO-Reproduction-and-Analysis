# Evaluation Results

## Sequences

Two M2DGR sequences were evaluated in this reproduction.

| Sequence | Evaluation Scope | APE RMSE (m) | APE Mean (m) | RPE RMSE (m) | RPE Mean (m) | Status |
|---|---|---:|---:|---:|---:|---|
| door_02 | position-based | 0.246345 | 0.226276 | 0.365113 | 0.218278 | success |
| room_01 | valid GT quaternion | 0.249044 | 0.241277 | 0.078890 | 0.064087 | success |

## Interpretation

The `door_02` sequence was successfully processed, but its downloaded ground-truth text file contains valid position values while the quaternion fields are all zeros. Therefore, its evo result is reported as a position-based trajectory evaluation.

The `room_01` sequence provides valid quaternion fields in the ground-truth file. Its evaluation is therefore more suitable as the main quantitative result. LOG-LIO achieved an APE RMSE of 0.249044 m and an RPE RMSE of 0.078890 m on this sequence after evo alignment.

## Generated Files

Evaluation tables:

- `results/error_tables/ape_door_02.txt`
- `results/error_tables/rpe_door_02.txt`
- `results/error_tables/ape_room_01.txt`
- `results/error_tables/rpe_room_01.txt`

Figures:

- `results/figures/door_02_trajectory_comparison.pdf`
- `results/figures/door_02_ape.pdf`
- `results/figures/door_02_rpe.pdf`
- `results/figures/room_01_trajectory_comparison.pdf`
- `results/figures/room_01_ape.pdf`
- `results/figures/room_01_rpe.pdf`

Summary table:

- `results/evaluation_summary.csv`
