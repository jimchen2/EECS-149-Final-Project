from ultralytics import YOLO
import subprocess
import threading

# Function to run the libcamera-vid command
def run_camera():
    cmd = "libcamera-vid -n -t 0 --width 1280 --height 960 --framerate 1 --inline --listen -o tcp://127.0.0.1:8888"
    subprocess.run(cmd, shell=True)

# Start the camera capture in a separate thread
camera_thread = threading.Thread(target=run_camera)
camera_thread.start()

# Load YOLO model
model = YOLO('yolov8n.pt')

# Process video stream
results = model('tcp://127.0.0.1:8888', stream=True)

while True:
    for result in results:
        # Extract boxes and probabilities
        boxes = result.boxes
        probs = result.probs

        # Print boxes and probabilities
        print("Boxes:", boxes)
        print("Probabilities:", probs)
