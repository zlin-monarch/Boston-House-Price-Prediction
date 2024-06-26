#!/usr/bin/env bash

## Complete the following steps to get Docker running locally
### Method 1: Build the Docker image and run the container
docker compose up --build 



### Method 2: Step by step
# Step 1:
# Build image and add a descriptive tag
docker build --tag=medv .

# Step 2:
# List docker images
docker image ls

# Step 3:
# Run streamlit app
docker run -p 8765:8765 medv
