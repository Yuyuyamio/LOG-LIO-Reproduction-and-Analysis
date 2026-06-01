# M2DGR Configuration Notes

## Sequences

| Sequence | Rosbag size | Role |
|---|---:|---|
| `door_02` | 9.8 GB | Successful run and position-level sanity check |
| `room_01` | 13.9 GB | Main quantitative sequence and ablation sequence |

## Required Topics

| Sensor | Topic |
|---|---|
| LiDAR | `/velodyne_points` |
| IMU | `/handsfree/imu` |

These topics were confirmed with `rosbag info` before running LOG-LIO.

## LOG-LIO Files Used

| Type | File |
|---|---|
| Launch file | `launch/mapping_m2dgr.launch` |
| Config file | `config/velodyne_m2dgr.yaml` |

## Notes

`door_02` provides valid position values but invalid quaternion fields in the downloaded ground-truth file, so it is used only as a position-level sanity check.

`room_01` is used as the main quantitative sequence. The no-surfel ablation is also based on `room_01`.
