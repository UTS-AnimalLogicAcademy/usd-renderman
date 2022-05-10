#! /bin/bash

export CC=/opt/rh/devtoolset-7/root/bin/gcc
export CXX=/opt/rh/devtoolset-7/root/bin/g++

# this will release the rez package
rez-release
