# Milestone 1 Report: Trash Collector Bot

## Progress So Far
- Completed hardware procurement.
- Completed assembling the robot kit.
- Configured `ssh`
- Scripted photo capture and cloud/CNN deployment.
- Trained Yolo on images

## Goals 

Building ML-based robot for trash collection; includes state machine vs. ML comparison, spatial localization, pathfinding. Aim: navigate, identify obstacles, and pick up trash.

## Course Topics
### FSM

![image](https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/174bcfe7-8111-407b-9c8c-0eb78aba4025)

See https://www.overleaf.com/read/zczqmvbfxknk#4f2916
### TinyML

Yolo-v5 on Raspberry Pi

### Sensors and Actuators
Sensors: Cameras, ultrasonic (optional).
Raspberry Pi: Processes images, computer vision.
Actuators: Motors, arms.
Control: Raspberry Pi, GPIO pins, sensor-based.

### Wireless Control and Communication

Remote Operation: Using `ssh` to control the robot in real time(optional)
Data Transmission/Reception: Sends/receives location, garbage status, operational updates for dynamic operation.


## Resources Acquired
- Raspberry Pi CanaKit
- Robot Car Kit (including a robotic arm)

## Schedule

11/27 Week: Finish integrating the camera with the robot navigation. Implement a navigation method on the robot.

12/04 Week: Conduct debugging. Write report and prepare presentation.

- Jiamu: Python scripts for tinyML and photography, Yolo-v5 training/deployment, documentation, report writing.
- Samyak: Assist in robot assembly, implement spatial localization and navigation.
- Hanson: Assemble power, mechanical structure, setup microSD system, integrate ML model with robot functions.


## Risks Identified
Raspberry Pi OS Problems: Issues with cv2, lack of camera support, Python environment limitations, and an unsatisfactory package manager.
Robot Control Issues: Inadequate code from Adeept Bot for controlling the robot's claws and wheels.

## Repositories
- GitHub: [EECS-149 Final Project Repository](https://github.com/jimchen2/EECS-149-Final-Project)
- Gitbook: [EECS-149 Final Project Docs](https://berkeley-7.gitbook.io/pro/)
