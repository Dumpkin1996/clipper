#!/usr/bin/env bash
#/bin/sh

docker build -f ./prediction_wo_proxy/Dockerfile0.2 -t zsxhku/stock:container0.2 .
docker build -f ./prediction_wo_proxy/Dockerfile1.2 -t zsxhku/stock:container1.2 .
docker build -f ./prediction_wo_proxy/Dockerfile2.2 -t zsxhku/stock:container2.2 .
docker build -f ./prediction_wo_proxy/Dockerfile3.2 -t zsxhku/stock:container3.2 .
docker build -f ./prediction_wo_proxy/Dockerfile4.2 -t zsxhku/stock:container4.2 .
docker build -f ./prediction_wo_proxy/Dockerfile5.2 -t zsxhku/stock:container5.2 .
docker build -f ./prediction_wo_proxy/Dockerfile6.2 -t zsxhku/stock:container6.2 .
docker build -f ./prediction_wo_proxy/Dockerfile7.2 -t zsxhku/stock:container7.2 .
docker build -f ./prediction_wo_proxy/Dockerfile8.2 -t zsxhku/stock:container8.2 .
docker build -f ./prediction_wo_proxy/Dockerfile9.2 -t zsxhku/stock:container9.2 .
docker build -f ./prediction_wo_proxy/Dockerfile10.2 -t zsxhku/stock:container10.2 .
docker build -f ./prediction_wo_proxy/Dockerfile11.2 -t zsxhku/stock:container11.2 .
