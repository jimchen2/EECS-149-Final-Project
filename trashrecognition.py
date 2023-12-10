import torch
from torchvision import transforms
import cv2
import sys

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/pi/best.pt')

# Append path to sys
sys.path.append('/home/pi/EECS-149-Final-Project/scripts')

# Import the function to capture numpy image
from capture_numpy_image import capture_numpy_image

# Capture the image
numpy_image = capture_numpy_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)

# Convert BGR (OpenCV default) to RGB if necessary
numpy_image_rgb = cv2.cvtColor(numpy_image, cv2.COLOR_BGR2RGB)

# Convert numpy image to PyTorch tensor
tensor_image = transforms.ToTensor()(numpy_image_rgb).unsqueeze_(0)

# Get predictions from the model
predictions = model(tensor_image)

# Define a confidence threshold (e.g., 0.25)
confidence_threshold = 0.25

# Process the predictions
for detection in predictions[0]:
    # Extract information from the detection
    x_center, y_center, width, height, confidence, class_id = detection

    # Check if the confidence is above the threshold
    if confidence >= confidence_threshold:
        # Convert center coordinates (x_center, y_center) and size (width, height) to corner coordinates (xmin, ymin, xmax, ymax)
        xmin = x_center - (width / 2)
        ymin = y_center - (height / 2)
        xmax = x_center + (width / 2)
        ymax = y_center + (height / 2)

        print(f"Object Detected: Class ID - {class_id}, Confidence - {confidence:.2f}")
        print(f"Bounding Box Coordinates: xmin - {xmin}, ymin - {ymin}, xmax - {xmax}, ymax - {ymax}")

        # Draw bounding boxes on the image
        cv2.rectangle(numpy_image_rgb, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)

# At this point, you can display the image using cv2.imshow() or save it using cv2.imwrite(), 
# depending on your requirements.
