#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath="veraz00/price_prediction:v1"

# Step 2: 
# Create deployment
kubectl create deployment priceprediction  --image=veraz00/prediction:v1 

# Step 3:
# Scale the deployment
kubectl scale deployment/priceprediction --replicas=3


# Step 4:
# List kubernetes pods
kubectl get pods

# Step 5:
# Build a service to expose the deployment
kubectl expose deployment/priceprediction --type=LoadBalancer --name=priceprediction --port=8765 --target-port=5678
minikube service priceprediction 


