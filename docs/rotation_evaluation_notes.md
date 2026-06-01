# Rotation Evaluation Notes

Rotation APE/RPE is not reported in this reproduction.

The `room_01` ground-truth file contains non-zero quaternion values, but direct rotation comparison with the LOG-LIO output produced unrealistic errors. Several quaternion-order and inverse-quaternion checks were tested, but the rotation error remained abnormally large.

This suggests that the ground-truth orientation frame and the LOG-LIO output pose frame are not directly comparable without further frame-convention verification.

Therefore, this project reports translation-based APE/RPE as the reliable quantitative result. Full rotation evaluation is left for future work after confirming the exact transformation between the M2DGR ground-truth frame and the LOG-LIO output frame.
