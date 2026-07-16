# Autonomous Smart Wheelchair with Dual-LiDAR Collision Avoidance

A ROS 2 simulation of an autonomous smart wheelchair equipped with two LiDAR
sensors for mapping and obstacle detection. The robot is modelled in URDF/Xacro,
simulated in Gazebo, and localized/mapped using Google Cartographer in 3D.

This repository contains the `whintel_description` ROS 2 package: the robot
description (mesh + URDF), the simulation world, sensor transforms, and the
Cartographer configuration used to build a 3D map from the onboard sensors.
## Demo video

[![Watch the demo](https://www.youtube.com/watch?v=449FNtofZic/hqdefault.jpg)](https://www.youtube.com/watch?v=449FNtofZic)


## Features

- URDF/Xacro model of the wheelchair (`whintel.xacro`) with STL meshes for the
  base and wheels.
- Dual-LiDAR layout published as static transforms (`la_1` and `lb_1`), mounted
  symmetrically front and rear of `base_link`.
- Gazebo simulation using a custom test world (`worlds/test23.world`).
- 3D SLAM with Cartographer (`config/cartographer_3d.lua`), fusing point-cloud
  and IMU data with online correlative scan matching.
- Launch files for visualization (RViz), Gazebo bring-up, and SLAM.

## Package layout

```
whintel_description/
├── config/
│   └── cartographer_3d.lua        # Cartographer 3D SLAM configuration
├── launch/
│   ├── cartographer_3d.launch.py  # Starts Cartographer + occupancy grid node
│   ├── display.launch.py          # RViz visualization of the robot model
│   ├── gazebo.launch.py           # Spawns the robot in Gazebo
│   ├── static_tf.launch.py        # Publishes the dual-LiDAR static transforms
│   └── wheelchair_world.launch.py # Launches Gazebo with the custom world
├── meshes/                        # STL meshes (base_link, wheels, LiDAR arms)
├── urdf/
│   ├── whintel.xacro              # Main robot description
│   ├── whintel.gazebo             # Gazebo material / plugin definitions
│   ├── whintel.trans              # Transmission definitions
│   └── materials.xacro
└── worlds/
    └── test23.world               # Gazebo simulation world
```

## Requirements

- ROS 2 (developed on a distribution with `gazebo_ros`; e.g. Humble/Foxy)
- Gazebo (`gazebo_ros`)
- `xacro`
- `cartographer_ros`
- `robot_state_publisher`, `joint_state_publisher`, `tf2_ros`

## Build

Clone the package into the `src` folder of a ROS 2 workspace and build with colcon:

```bash
cd ~/ros2_ws/src
git clone https://github.com/PaONEkaruchola/Autonomous-Smart-Wheelchair-with-Dual-Lidar-Collision-Avoidance-.git
cd ~/ros2_ws
colcon build --packages-select whintel_description
source install/setup.bash
```

## Running

Visualize the model in RViz:

```bash
ros2 launch whintel_description display.launch.py
```

Spawn the wheelchair in the Gazebo world:

```bash
ros2 launch whintel_description wheelchair_world.launch.py
```

Publish the dual-LiDAR transforms and start 3D SLAM:

```bash
ros2 launch whintel_description static_tf.launch.py
ros2 launch whintel_description cartographer_3d.launch.py
```

## Known issues / notes

- **Hardcoded absolute paths:** some launch files and the Cartographer config
  reference machine-specific paths such as
  `/home/pavan/p3_ws/src/whintel_description/...`. These need to be updated to
  match your own workspace (or replaced with package-relative paths) before the
  launch files will work on another machine. Affected files include
  `launch/cartographer_3d.launch.py` and `launch/wheelchair_world.launch.py`.
- The Cartographer topic remappings (`/points2`, `/imu`, `/odom`) assume the
  simulated sensor topic names; adjust them to match your sensor setup.

## Demo

`Is.mp4` in the repository root shows the wheelchair operating in simulation.

## Author

Pavan Karuchola — https://github.com/PaONEkaruchola
Krishna Digamarthi - https://github.com/DKrishna007
