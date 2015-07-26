#!/bin/bash

git submodule init
git submodule update

path=`pwd`

cd $path/lib/python-bitcoinlib/
python3 setup.py install

cd $path/lib/bottle/
python3 setup.py install

