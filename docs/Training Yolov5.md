# Using ```yolo```

First basic setup methods
```
git clone https://github.com/ultralytics/ultralytics && cd yolov5
python -m venv yolov5-env
source yolov5-env/bin/activate
pip install -r requirements.txt
```

## Trying Out ```yolo```
```
IMAGE_PATH="$HOME/Downloads/1.png"
python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source "$IMAGE_PATH" --save-txt --save-conf
```
Adjust the image resolution and confident.

## ```yolo``` from Pretrained Datasets

The output from a image I took at Moffit.

As we can see it isn't very accurate (falsely labeling kite, and not including the flyers).

We need to make it label the flyers(and relevant stuff), to make it detect trash accordingly, then use the robot arm.

<img src="https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/048fa871-c2aa-47af-a1ce-243a573c8d3c" style="width: 50%;">

## Approach

# YOLO Trash Detection Workflow

## Step 1: Dataset Acquisition
- Find relevant datasets (e.g., TACO, Open Images).
- Optionally, supplement with custom data.

## Step 2: Automated Labeling
- Use a high-accuracy model like Mask R-CNN to assist in initial labeling.

## Step 3: Train YOLO Model
- Train YOLO using the labeled dataset.
- Split data: 70% training, 15% validation, 15% test.
- Adjust hyperparameters and apply data augmentation to improve model robustness.

