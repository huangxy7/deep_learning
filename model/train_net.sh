#!/usr/bin/env sh
set -e



/home/jsj/caffe/build/tools/caffe train --solver=/home/jsj/xytest/model/solver.prototxt 

#-snapshot=/home/jsj/traffic_light/data/models/snapshots/train_squeezenet_scratch__iter_13000.solverstate

