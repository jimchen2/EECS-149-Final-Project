from ultralytics import YOLO

model = YOLO('yolov5n.pt')
results = model('tcp://127.0.0.1:8888', stream=True)

while True:
    for result in results:
        boxes = result.boxes
        probs = result.probs
