# Environment Notes

| Item          | Setting               |
| ------------- | --------------------- |
| Host          | Windows + WSL2 Ubuntu |
| Runtime       | Docker container      |
| ROS           | Noetic                |
| Build system  | catkin                |
| Dataset       | M2DGR                 |
| Evaluation    | evo                   |
| Visualization | RViz with WSLg        |

LOG-LIO was built and tested inside a ROS Noetic Docker environment.

The main LOG-LIO workspace was:

```text
/root/slam_ws
```

Large dataset files such as `.bag` files are excluded from this repository.
