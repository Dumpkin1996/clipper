#/bin/bash

docker build -f ./auto_pilot/Dockerfile0.2 -t auto_pilot:container0.2 .
docker build -f ./auto_pilot/Dockerfile1.2 -t auto_pilot:container1.2 .
docker build -f ./auto_pilot/Dockerfile2.2 -t auto_pilot:container2.2 .
docker build -f ./auto_pilot/Dockerfile3.2 -t auto_pilot:container3.2 .
docker build -f ./auto_pilot/Dockerfile4.2 -t auto_pilot:container4.2 .
docker build -f ./auto_pilot/Dockerfile5.2 -t auto_pilot:container5.2 .
docker build -f ./auto_pilot/Dockerfile6.2 -t auto_pilot:container6.2 .