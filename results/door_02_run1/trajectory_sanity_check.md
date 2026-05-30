# Trajectory Sanity Check: M2DGR door_02

Input file:
results/door_02_run1/target_path.txt

Basic statistics:
- Valid trajectory rows: 2469
- Start timestamp: 1628062054.858837
- End timestamp: 1628062181.706238
- Duration: 126.847 s

Position range:
- x range: -0.229 m to 29.418 m
- y range: -16.733 m to 0.052 m
- z range: 0.833 m to 2.129 m

Start position:
- x: 0.133358
- y: -0.007417
- z: 0.838714

End position:
- x: 23.269055
- y: -15.273051
- z: 2.069970

Net displacement:
- dx: 23.136 m
- dy: -15.266 m
- dz: 1.231 m
- 3D displacement: 27.746 m

Estimated trajectory length:
- accumulated path length: 70.413 m

Interpretation:
The trajectory file is non-empty and covers the full rosbag time range.
The position changes over time, so LOG-LIO did not merely start and stop; it produced an odometry trajectory for the door_02 sequence.
This result is suitable for the next phase: trajectory visualization and qualitative analysis.
