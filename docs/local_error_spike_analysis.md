# Local Error Spike Analysis

## Scope

No complete tracking failure was observed in the current reproduction. Both `door_02` and `room_01` were successfully processed by LOG-LIO and produced trajectory outputs.

This file therefore focuses on short-term local error spikes rather than system-level tracking failure.

## Evidence

The main quantitative sequence is `room_01`, because it was used for both the baseline run and the no-surfel ablation comparison.

| Sequence  | Setting   | APE RMSE (m) | APE Mean (m) | RPE RMSE (m) | RPE Mean (m) | RPE Max (m) |
| --------- | --------- | -----------: | -----------: | -----------: | -----------: | ----------: |
| `room_01` | baseline  |     0.249044 |     0.241277 |     0.078890 |     0.064087 |    0.614137 |
| `room_01` | no-surfel |     0.246773 |     0.238837 |     0.075243 |     0.059319 |    0.612164 |

The APE values show that the global translation error remains moderate after alignment. The RPE mean and RMSE are also relatively small, suggesting that the local motion estimation is mostly stable.

However, the RPE maximum is much larger than the RPE mean. This indicates that at least one short local segment may contain a larger relative-motion error spike.

## Possible Causes

The current repository does not identify the exact timestamp of the local RPE spike. Possible explanations include:

* weak local geometric structure,
* short-term LiDAR-IMU synchronization error,
* fast local rotation or motion,
* temporary reduction in useful scan constraints,
* parameter mismatch for this indoor sequence.

## Conclusion

The current results do not indicate a complete LOG-LIO tracking failure. The `room_01` trajectory is usable for reproduction analysis, and the RViz visualization also shows a coherent local point-cloud map.

The main limitation is that this analysis is based on evaluation statistics and visual inspection, not on a manually localized error segment. A stronger analysis would require identifying the exact timestamp where the RPE spike occurs and checking the corresponding LiDAR geometry, motion condition, and data association behavior.
