#!/usr/bin/bash

python3 -m grpc_tools.protoc -I ./stepth-protos/ --python_out=./stepthui_py/ --grpc_python_out=./stepthui_py/ ./stepth-protos/stepth.proto
