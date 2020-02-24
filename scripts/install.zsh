#!/bin/zsh

script_dir=$(cd $(dirname $0); pwd)

d=ros-dashing
p=python3
pkgs=("${d}-joy" "${p}-argcomplete" "${p}-colcon-common-extensions")

if ! dpkg-query -W ${pkgs[@]} &> /dev/null; then
    sudo -E apt install ${pkgs[@]}
else
    echo "All required apt packages are installed"
fi

if ! grep "tori ()" ~/.zshrc &> /dev/null; then
    cat ${script_dir}/zshrc >> ~/.zshrc
else
    echo "zshrc has been set up already."
fi
