#!/bin/bash

image_name=10.161.31.82:5000/phm/enas/serve
image_tag=latest
full_image_name=${image_name}:${image_tag}
cd "$(dirname "$0")"

docker build -t "${full_image_name}" .
docker push ${full_image_name}
docker inspect --format="{{index .RepoDigests 0}}" "${full_image_name}"