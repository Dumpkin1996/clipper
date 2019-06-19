#!/usr/bin/env bash
#/bin/sh

docker build -f ./prediction_w_proxy/Dockerfile0 -t zsxhku/stock:container0 .
docker build -f ./prediction_w_proxy/Dockerfile1 -t zsxhku/stock:container1 .
docker build -f ./prediction_w_proxy/Dockerfile2 -t zsxhku/stock:container2 .
docker build -f ./prediction_w_proxy/Dockerfile3 -t zsxhku/stock:container3 .
docker build -f ./prediction_w_proxy/Dockerfile4 -t zsxhku/stock:container4 .
docker build -f ./prediction_w_proxy/Dockerfile5 -t zsxhku/stock:container5 .
docker build -f ./prediction_w_proxy/Dockerfile6 -t zsxhku/stock:container6 .
docker build -f ./prediction_w_proxy/Dockerfile7 -t zsxhku/stock:container7 .
docker build -f ./prediction_w_proxy/Dockerfile8 -t zsxhku/stock:container8 .
docker build -f ./prediction_w_proxy/Dockerfile9 -t zsxhku/stock:container9 .
docker build -f ./prediction_w_proxy/Dockerfile10 -t zsxhku/stock:container10 .
docker build -f ./prediction_w_proxy/Dockerfile11 -t zsxhku/stock:container11 .
