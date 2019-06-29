#!/bin/bash

INIT_DIR="$(pwd)"
cd "${INIT_DIR}/myapp" && zip -r myapp.zip *.py >/dev/null
mv "${INIT_DIR}/myapp/myapp.zip" "${INIT_DIR}/myapp.zip"
cd "${INIT_DIR}"

python3 myapp.zip
