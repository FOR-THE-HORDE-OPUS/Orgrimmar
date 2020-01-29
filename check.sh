#!/bin/sh
echo Input threshold
read threshold
export threshold=$threshold
env/bin/python3  ./core/tf.py