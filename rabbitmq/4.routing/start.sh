#!/bin/bash

python3 recv_log.py info &

for i in $(seq 1 10); do
    python3 emit_log.py
done
