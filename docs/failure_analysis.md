# Failure and Drift Analysis

## Scope

This file records the current failure/drift analysis based on the reproduced M2DGR sequences.

At this stage, no complete tracking failure was observed. Both `door_02` and `room_01` were successfully processed by LOG-LIO and produced trajectory outputs.

Therefore, this analysis focuses on potential short-term drift instead of claiming a full system failure.

## Current Evidence

The `room_01` sequence provides valid ground-truth quaternion values and is the main quantitative evaluation sequence.

For `room_01`, the evo results are:

| Metric | Value |
|---|---:|
| APE RMSE | 0.249044 m |
| APE Mean | 0.241277 m |
| APE Max | 0.359053 m |
| RPE RMSE | 0.078890 m |
| RPE Mean | 0.064087 m |
| RPE Max | 0.614137 m |

The APE result suggests that the global trajectory error is moderate after alignment. The RPE mean and RMSE are also relatively small, which indicates that the local motion estimation is mostly stable.

However, the RPE maximum value is much larger than the RPE mean. This suggests that at least one local segment may contain a short-term error spike.

## Possible Causes

The current data is not enough to identify the exact cause of the RPE spike. Possible explanations include:

1. weak local geometric structure,
2. short-term LiDAR-IMU synchronization error,
3. fast local motion,
4. temporary reduction in useful scan constraints,
5. parameter mismatch for this indoor sequence.

## Current Conclusion

The current reproduction does not show a complete LOG-LIO failure. The `room_01` result is usable and stable enough for reproduction analysis.

The main limitation is that the current failure analysis is based on evaluation statistics and plots, not on a manually localized failure frame. A stronger failure analysis would require inspecting the RPE curve and trajectory plot to identify the exact timestamp or segment where the local error spike occurs.
