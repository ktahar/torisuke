import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch.actions
import launch_ros.actions

def generate_launch_description():

    parameters_file = os.path.join(
        get_package_share_directory('tori_tools'),
        'config', 'logi_f310.yaml'
    )

    ld = LaunchDescription([
        launch.actions.DeclareLaunchArgument('teleop_config', default_value=parameters_file),
    ])

    ld.add_action(launch_ros.actions.Node(
            package='joy', node_executable='joy_node',
            output='screen'))

    ld.add_action(launch_ros.actions.Node(
            package='joy_teleop', node_executable='joy_teleop',
            output='screen',
            parameters=[launch.substitutions.LaunchConfiguration('teleop_config')]))

    return ld
