#!/bin/bash

docker build -t test/flaskapp .
docker run test/flaskapp
curl http://localhost:9090/
