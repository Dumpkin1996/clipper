#!/usr/bin/env bash
#/bin/sh

docker build -f ./prediction/Dockerfile0.2 -t zsxhku/stock:container0.2 .
docker build -f ./prediction/Dockerfile1.2 -t zsxhku/stock:container1.2 .
docker build -f ./prediction/Dockerfile2.2 -t zsxhku/stock:container2.2 .
docker build -f ./prediction/Dockerfile3.2 -t zsxhku/stock:container3.2 .
docker build -f ./prediction/Dockerfile4.2 -t zsxhku/stock:container4.2 .
docker build -f ./prediction/Dockerfile5.2 -t zsxhku/stock:container5.2 .
docker build -f ./prediction/Dockerfile6.2 -t zsxhku/stock:container6.2 .
docker build -f ./prediction/Dockerfile7.2 -t zsxhku/stock:container7.2 .
docker build -f ./prediction/Dockerfile8.2 -t zsxhku/stock:container8.2 .
docker build -f ./prediction/Dockerfile9.2 -t zsxhku/stock:container9.2 .
docker build -f ./prediction/Dockerfile10.2 -t zsxhku/stock:container10.2 .
docker build -f ./prediction/Dockerfile11.2 -t zsxhku/stock:container11.2 .
