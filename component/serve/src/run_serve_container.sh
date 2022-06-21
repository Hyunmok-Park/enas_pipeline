#!/bin/sh

cd data
bentoml import enas_pipeline.bento
bentoml serve enas_pipeline:latest --production
