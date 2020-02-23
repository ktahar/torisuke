#!/bin/zsh

d=ros-dashing
p=python3
pkgs=("${d}-joy" "${p}-argcomplete" "${p}-colcon-common-extensions")

if ! dpkg-query -W ${pkgs[@]} &> /dev/null; then
    sudo -E apt install ${pkgs[@]}
else
    echo "All required apt packages are installed"
fi

col="source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.zsh"
if ! grep $col ~/.zshrc &> /dev/null; then
    echo $col >> ~/.zshrc
else
    echo "colcon-argcomplete has been set up already."
fi
