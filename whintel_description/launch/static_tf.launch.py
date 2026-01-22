from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_la',
            arguments=['0.92', '0.0', '0.3', '0', '0', '0', 'base_link', 'la_1']
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_lb',
            arguments=['-0.92', '0.0', '0.3', '0', '0', '0', 'base_link', 'lb_1']
        ),
    ])

