import sys
sys.path.append('/opt/ros/jazzy/lib/python3.12/site-packages')  # adjust python version


import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    # Path to an empty Gazebo world
    gazebo_world_path = "/usr/share/gazebo/worlds/empty.world"

    return LaunchDescription([
        # Launch Gazebo with empty world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', gazebo_world_path],
            output='screen'
        )
    ])


generate_launch_description()