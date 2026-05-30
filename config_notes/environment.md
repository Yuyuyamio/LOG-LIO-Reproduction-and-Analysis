# Environment Notes

## 1. Current Stage

At this stage, the repository is prepared on Windows. The actual LOG-LIO build and ROS execution should be performed in an Ubuntu / ROS environment.

The Windows system is mainly used for:
- writing documentation
- organizing the reproduction repository
- preparing scripts
- managing GitHub files

The Ubuntu / ROS environment will be used for:
- cloning and building the official LOG-LIO source code
- running catkin_make
- launching LOG-LIO
- playing M2DGR rosbag files
- saving trajectory and RViz results

---

## 2. Target Reproduction Environment

Recommended environment:

- Operating System: Ubuntu 20.04
- ROS Version: ROS Noetic
- Build System: catkin
- Main Tools:
  - CMake
  - GCC / G++
  - PCL
  - Eigen
  - Python 3
  - evo for trajectory evaluation

---

## 3. Important Version Note

ROS Noetic was designed mainly for Ubuntu 20.04, so Ubuntu 20.04 + ROS Noetic is the safest environment for reproducing this older ROS 1 project.

However, ROS Noetic has reached end-of-life. For this project, it is still acceptable because the goal is academic reproduction of an existing ROS 1 SLAM system, not long-term deployment.

---

## 4. Recommended Setup Choice

Preferred option:

Use Ubuntu 20.04 directly, either on:
- a native Ubuntu installation
- a dual-boot system
- a virtual machine with enough RAM and disk space

Possible but less ideal option:

Use WSL2 on Windows. This may work for compiling and command-line experiments, but RViz and graphics-related tools may create extra problems.

For this reproduction project, a real Ubuntu 20.04 environment is cleaner and easier to explain in the report.

---

## 5. Planned Workspace

The official LOG-LIO code should be cloned into a ROS workspace, not copied into this reproduction repository.

Planned workspace on Ubuntu:

```bash
mkdir -p ~/slam_ws/src
cd ~/slam_ws/src
git clone https://github.com/tiev-tongji/LOG-LIO.git
cd ..
catkin_make
source devel/setup.bash
```

---

## 6. Repository Strategy

The reproduction repository only stores:

- notes
- scripts
- configuration records
- result tables
- figures
- final report

The official LOG-LIO source code is used locally for building and testing, but it is not copied into this repository.

---

## 7. Environment Checklist

- [ ] Ubuntu 20.04 environment ready
- [ ] ROS Noetic installed
- [ ] catkin workspace created
- [ ] official LOG-LIO repository cloned locally
- [ ] dependencies installed
- [ ] catkin_make executed
- [ ] build errors recorded in troubleshooting/ros_build_errors.md
- [ ] source devel/setup.bash tested
