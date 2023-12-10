import torch
from torchvision import transforms
import cv2
import sys
import numpy as np

# Load the YOLOv5 model once, outside the main function
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/pi/best.pt')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Append path to sys
sys.path.append('/home/pi/EECS-149-Final-Project/scripts')

# Import necessary functions
from capture_numpy_image import capture_numpy_image
from upload_to_dropbox import upload_image_to_dropbox

def main():
    # Capture the image
    numpy_image = capture_numpy_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)

    # Convert BGR (OpenCV default) to RGB if necessary
    numpy_image_rgb = cv2.cvtColor(numpy_image, cv2.COLOR_BGR2RGB)

    # Convert numpy image to PyTorch tensor
    tensor_image = transforms.ToTensor()(numpy_image_rgb).unsqueeze_(0)

    # Get predictions from the model
    predictions = model(tensor_image)

    # Define a confidence threshold
    confidence_threshold = 0.05

    # Process the predictions
    for detection in predictions[0]:
        # Extract information from the detection
        if len(detection) >= 6:
            x_center, y_center, width, height, confidence, class_id, *_ = detection
    
            # Check if the confidence is above the threshold
            if confidence >= confidence_threshold:
                # Convert coordinates and draw bounding boxes
                xmin, ymin, xmax, ymax = convert_to_corner_coordinates(x_center, y_center, width, height)
                cv2.rectangle(numpy_image_rgb, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)

    # Convert the processed numpy image to a JPEG byte stream
    _, buffer = cv2.imencode('.jpg', numpy_image_rgb)
    jpeg_image_byte_stream = np.array(buffer).tobytes()

    # Upload the JPEG byte stream to Dropbox
    upload_image_to_dropbox(jpeg_image_byte_stream, is_numpy=False)

def convert_to_corner_coordinates(x_center, y_center, width, height):
    """Convert center coordinates and size to corner coordinates."""
    xmin = x_center - (width / 2)
    ymin = y_center - (height / 2)
    xmax = x_center + (width / 2)
    ymax = y_center + (height / 2)
    return xmin, ymin, xmax, ymax

# Execute the main function
if __name__ == "__main__":
    main()
