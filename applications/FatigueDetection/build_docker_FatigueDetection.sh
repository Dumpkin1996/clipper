#!/usr/bin/env bash
#/bin/sh

chmod 777 ./FatigueDetection/container2/app/dl.sh
chmod 777 ./FatigueDetection/container3/app/dl.sh
chmod 777 ./FatigueDetection/container4/app/dl.sh
./FatigueDetection/container2/app/dl.sh
./FatigueDetection/container3/app/dl.sh
./FatigueDetection/container4/app/dl.sh


docker build -f ./FatigueDetection/Dockerfile0 -t detection:container0 .
docker build -f ./FatigueDetection/Dockerfile1 -t detection:container1 .
docker build -f ./FatigueDetection/Dockerfile2 -t detection:container2 .
docker build -f ./FatigueDetection/Dockerfile3 -t detection:container3 .
docker build -f ./FatigueDetection/Dockerfile4 -t detection:container4 .

