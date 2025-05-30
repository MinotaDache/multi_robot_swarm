
from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node 
import os
from launch.substitutions import Command 
from ament_index_python.packages import get_package_share_path
# we first define the launch description

def generate_launch_description():

    # Get the path of urdf file with out xacro     
    """urdf_file = os.path.join(get_package_share_path('amr_swarming_description'), 
                             'urdf', 'mrobot.urdf')"""
    # get the urdf file with xacro modifications
    urdf_file = os.path.join(get_package_share_path('amr_swarming_description'), 
                             'urdf', 'robot.urdf.xacro')
    rviz_config_path = os.path.join(get_package_share_path('amr_swarming_description'),
                                    'rviz', 'urdf_config.rviz')

    robot_description = ParameterValue(Command(['xacro ', urdf_file]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': robot_description}]

    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_path]

    )   

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz2_node

    ])