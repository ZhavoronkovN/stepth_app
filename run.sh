#!/usr/bin/bash

kill $(ps -A | grep "stepth-server" | awk '{print $1}')
python3 -m grpc_tools.protoc -I ./stepth-protos/ --python_out=./stepthui_py/ --grpc_python_out=./stepthui_py/ ./stepth-protos/stepth.proto
cargo run --manifest-path ./stepth-server/Cargo.toml &
sleep 1
python3 ./stepthui_py/main.py
kill $(ps -A | grep "stepth-server" | awk '{print $1}')