import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
import launch.actions
import launch_ros.actions

def generate_launch_description():

    parameters_file = os.path.join(
        get_package_share_directory('tori_tools'),
        'config', 'driver.yaml'
    )

    ld = LaunchDescription([
        launch.actions.DeclareLaunchArgument('driver_config', default_value=parameters_file),
    ])

    ld.add_action(launch_ros.actions.Node(
            package='ca_driver', node_executable='ca_driver',
            parameters=[launch.substitutions.LaunchConfiguration('driver_config')]))

    return ld
