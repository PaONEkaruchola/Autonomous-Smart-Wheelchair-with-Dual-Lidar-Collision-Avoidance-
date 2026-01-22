from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': True}],
            arguments=[
                '-configuration_directory', '/home/pavan/p3_ws/src/whintel_description/config',
                '-configuration_basename', 'cartographer_3d.lua'
            ],
            remappings=[
                ('/points2', '/la/laser/scan'),  # LiDAR topic
                ('/imu', '/imu'),                # IMU topic
                ('/odom', '/odom')               # Odometry topic
            ]
        ),
        Node(
            package='cartographer_ros',
            executable='occupancy_grid_node',
            name='occupancy_grid_node',
            parameters=[{'use_sim_time': True}]
        )
    ])
