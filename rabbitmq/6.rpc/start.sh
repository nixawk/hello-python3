#!/bin/bash

python3 rpc_server.py &

for i in $(seq 1 10); do
    python3 rpc_client.py
done