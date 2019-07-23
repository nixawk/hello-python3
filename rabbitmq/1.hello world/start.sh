#!/bin/bash

for i in $(seq 1 10); do
    python3 send.py
done

python3 recv.py