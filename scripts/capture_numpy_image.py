import cv2
import numpy as np
from capture_image import capture_image

def capture_numpy_image(timeout=0, resolution=(0, 0), preview=True, hflip=False, quality=93):
    """
    Captures an image using libcamera-still and returns it as a numpy array.
    """
    image_data = capture_image(timeout=timeout, resolution=resolution, preview=preview, hflip=hflip, quality=quality)
    image_array = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    return image_array

# Example usage
# image_array = capture_numpy_image(timeout=1000, resolution=(640, 480), preview=False, hflip=True)

