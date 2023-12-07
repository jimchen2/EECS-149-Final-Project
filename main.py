import subprocess
import os
import torch

# Path to your YOLOv5 directory
yolov5_dir = '/home/pi/yolov5-rasp-pi'

# Start the libcamera-vid command
libcamera_cmd = [
    'libcamera-vid', '-n', '-t', '0',
    '--width', '1280', '--height', '960',
    '--framerate', '1', '--inline', '--listen',
    '-o', 'tcp://127.0.0.1:8888'
]
subprocess.Popen(libcamera_cmd)

# Load the YOLOv5 model
weights_path = os.path.join(yolov5_dir, 'best.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights_path)

# Define the source
source = 'tcp://127.0.0.1:8888'

# Perform detection
results = model(source)

# Process results to print bounding box information
for result in results.xyxy[0]:
    # Each result contains [x1, y1, x2, y2, confidence, class]
    x1, y1, x2, y2, conf, cls = result
    print(f"Bounding Box: x1={x1}, y1={y1}, x2={x2}, y2={y2}, Confidence: {conf}, Class: {cls}")
