#!/bin/bash

python3 recv_log.py &


for i in $(seq 1 5); do
    python3 emit_log.py
done