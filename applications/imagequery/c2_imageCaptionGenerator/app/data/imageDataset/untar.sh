#!/bin/bash
# The following line is crucial, otherwise when called in Dockerfile, pwd still gives "/"
cd /container/data/imageDataset
tar xzf ./101_ObjectCategories.tar.gz