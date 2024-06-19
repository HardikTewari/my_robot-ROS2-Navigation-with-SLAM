## Navigation of personalized robot using ros2 and SLAM 

* my_robot_description - contains the files for visualising the robot on rviz2
* my_robot_bringup - contains the files for launching the robot on gazebo
* my_robot_teleoperator - contains the files for controlling the robot in gazebo simulation
* my_robot_navigation - contains the files for autonomous navigation using SLAM

## Steps for navigation of robot

* If needed, launch the robot in rviz2 first for visualization with
```
$ ros2 launch my_robot_description display.launch.xml
```

* For starting the robot in Gazebo, use
```
$ ros2 launch my_robot_bringup my_robot_gazebo.launch.xml
```

* For controller the robot in gazebo
```
$ ros2 launch my_robot_teleoperator teleop_launch.py
```

* Start the slam with
```
$ ros2 launch my_robot_navigation slam_launch.py
```

* After generating the map, start the autonomous navigation with
```
$ ros2 launch my_robot_navigation nav_launch.py
```

## Multi-robot-navigation

*launch the robots using
```
$ ros2 launch multi_robot_navigation gazebo_multi_nav2_world.launch.py
```

