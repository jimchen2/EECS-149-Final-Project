import os

def convert_bbox(image_width, image_height, x_min, y_min, x_max, y_max):
    dw = 1./image_width
    dh = 1./image_height
    x = (x_min + x_max) / 2.0
    y = (y_min + y_max) / 2.0
    w = x_max - x_min
    h = y_max - y_min
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return [x, y, w, h]

# Set the path to your labels directory
label_dir = './labels/test'

# Assuming all images have the same dimensions
image_width = 1280  # Replace with your image width
image_height = 720  # Replace with your image height

# Class ID for 'Tin can'
class_id_for_tin_can = 0  # Replace with the correct class ID if different

# Process each file in the directory
for filename in os.listdir(label_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(label_dir, filename)
        with open(file_path, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            if line.startswith('Tin can'):
                # Extract coordinates
                coordinates = line[7:].strip().split()
                x_min, y_min, x_max, y_max = map(float, coordinates)
                yolo_format = convert_bbox(image_width, image_height, x_min, y_min, x_max, y_max)
                new_lines.append(f"{class_id_for_tin_can} {' '.join(map(str, yolo_format))}\n")

        with open(file_path, 'w') as file:
            file.writelines(new_lines)

