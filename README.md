# torisuke

Hello, I'm torisuke.

## Requirements
- ROS2

## Notes on installation
- `python3-argcomplete`
- `python3-colcon-common-extensions`

## Notes on build

1. Install deps

```
cd ~/torisuke
rosdep update
rosdep install --from-paths src -i
```

2. Build

```
cd ~/torisuke
colcon build
```
