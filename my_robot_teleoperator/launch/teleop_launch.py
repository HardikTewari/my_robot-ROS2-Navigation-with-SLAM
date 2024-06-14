# teleop_launch.py

import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gnome-terminal', '--', 'ros2', 'run', 'teleop_twist_keyboard', 'teleop_twist_keyboard', '--ros-args', '--remap', 'cmd_vel:=/test/cmd_vel'],
            output='screen'
        ),
    ])
