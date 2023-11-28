#!/bin/bash

# Navigate to the YOLOv5 directory
cd yolov5

# Start the training
python train.py --img 640 --batch 16 --epochs 100 --data ../tincan.yaml --weights yolov5s.pt --cache

