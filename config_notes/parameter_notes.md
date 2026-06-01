# Parameter Notes

## Surfel Association Ablation

This note records a small ablation experiment on the M2DGR `room_01` sequence.

Baseline setting:

* `cloud_surfel: true`
* `point_surfel: true`

Ablation setting:

* `cloud_surfel: false`
* `point_surfel: false`

## Results

| Setting   | APE RMSE (m) | APE Mean (m) | RPE RMSE (m) | RPE Mean (m) |
| --------- | -----------: | -----------: | -----------: | -----------: |
| baseline  |     0.249044 |     0.241277 |     0.078890 |     0.064087 |
| no-surfel |     0.246773 |     0.238837 |     0.075243 |     0.059319 |

## Interpretation

On `room_01`, disabling surfel association did not degrade the result. The no-surfel setting produced slightly lower APE and RPE values, but the difference is small.

This result should not be interpreted as proof that surfel association is unnecessary. A safer conclusion is that the effect of surfel association is scene-dependent. For this short indoor sequence, the simpler association setting produced a very similar result.

A stronger conclusion would require testing more sequences and inspecting when surfel constraints are accepted or rejected in the code.
