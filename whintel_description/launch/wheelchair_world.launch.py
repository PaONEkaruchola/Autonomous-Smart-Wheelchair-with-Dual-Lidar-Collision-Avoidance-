#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, Command
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    gazebo_pkg = FindPackageShare("gazebo_ros")
    description_pkg = FindPackageShare("whintel_description")

    # Path to Xacro
    xacro_path = PathJoinSubstitution([
        description_pkg, "urdf", "whintel.xacro"
    ])

    return LaunchDescription([
    IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                gazebo_pkg, "launch", "gazebo.launch.py"
            ])
        ),
        launch_arguments={
            "world": "/home/pavan/p3_ws/src/whintel_description/worlds/test23.world",

             
            "verbose": "true"
        }.items()

        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    description_pkg, "launch", "static_tf.launch.py"
                ])
            )
        ),

        # Start robot_state_publisher using xacro
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{
                "robot_description": Command(["xacro ", xacro_path])
            }]
        ),

        # Spawn robot using /robot_description topic
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            name="spawn_wheelchair",
            output="screen",
            arguments=[
                "-entity", "wheelchair",
                "-topic", "robot_description",
                "-x", "0", "-y", "0", "-z", "0.3"
            ]
        ),
    ])

