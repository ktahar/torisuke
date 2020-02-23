#!/bin/zsh

d=ros-dashing
p=python3
pkgs=("${d}-joy" "${p}-argcomplete" "${p}-colcon-common-extensions")

if ! dpkg-query -W ${pkgs[@]} &> /dev/null; then
    sudo -E apt install ${pkgs[@]}
else
    echo "All required apt packages are installed"
fi
