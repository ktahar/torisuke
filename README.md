# torisuke

Hello, I'm torisuke.

## Install
- ROS2 Dashing
- `python3-argcomplete`
- `python3-colcon-common-extensions`

## Build

1. Install deps

```bash
cd ~/torisuke
rosdep update
rosdep install --from-paths src -i
```

or `scripts/install.zsh`

```bash
cd ~/torisuke
scripts/install.zsh
```

2. Build

```bash
cd ~/torisuke
colcon build
```

### On Raspberry Pi
On rpi, out of memory could occur and entire system can be down.

1. Limit by build option.

```bash
MAKEFLAGS="-j1 -l1" colcon build --executor sequential
```

2. Create swap area. See [this article](https://bogdancornianu.com/change-swap-size-in-ubuntu/).

```bash
sudo swapoff -a
sudo dd if=/dev/zero of=/swapfile bs=500M count=8 # 4 GB
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Edit `/etc/fstab` and append following line.
```
/swapfile swap swap defaults 0 0
```
