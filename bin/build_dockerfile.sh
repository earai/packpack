#!/usr/bin/env bash

cd $(git rev-parse --show-toplevel)

docker build -t packpack:latest .