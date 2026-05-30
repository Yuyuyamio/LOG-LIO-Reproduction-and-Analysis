# Runtime Log Analysis: M2DGR door_02

## 1. Purpose

This document analyzes the runtime log generated during the LOG-LIO reproduction run on the M2DGR `door_02` sequence.

The input file is:

results/door_02_run1/fast_lio_time_log.csv

The goal is to understand the per-frame processing behavior recorded by LOG-LIO, rather than only checking whether a trajectory file was generated.

## 2. Runtime Log Fields

The CSV file records the following fields:

- time_stamp
- total time
- scan point size
- incremental time
- search time
- delete size
- delete time
- tree size st
- tree size end
- add point size
- preprocess time

These values describe the frame timestamp, point cloud size, map update cost, and other runtime-related information.

## 3. Basic Runtime Statistics

For the `door_02` run, the runtime log contains:

- Logged frames: 1268
- Average total processing time per frame: 0.0724 s
- Average scan point size: 12043.1 points
- Average incremental map update time: 0.0116 s
- Average preprocess time: 0.0150 s
- Average added map points per frame: 1022.19 points
- Average search time: 0 s
- Average delete time: 0 s

## 4. Interpretation

The runtime log confirms that LOG-LIO processed a large number of LiDAR frames during the `door_02` sequence. The average scan size is about 12000 points per frame, which is reasonable for a Velodyne-style LiDAR sequence after topic filtering and preprocessing.

The average total processing time per logged frame is about 0.0724 s. This shows that the system completed not only trajectory estimation but also produced frame-level timing information.

The preprocess time and incremental map update time are both nonzero. This means the run included actual point cloud preprocessing and active map maintenance, rather than only reading messages or producing an empty output.

The average added point size is about 1022 points per frame. This supports that the local map was continuously updated during the run.

The search time and delete time columns are recorded as 0 in this log. This should not be interpreted as proof that searching and deletion have no computational cost. A safer interpretation is that these values were not measured or not written as nonzero values in this logging configuration.

## 5. Current Conclusion

The runtime analysis supports the reproduction result from another angle. LOG-LIO successfully processed the M2DGR `door_02` sequence, generated a trajectory, and recorded per-frame processing information.

At this stage, the runtime log is useful for basic engineering verification. Later work could compare these values across different datasets, parameter settings, or modified association strategies.
