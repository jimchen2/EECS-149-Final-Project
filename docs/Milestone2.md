# Milestone 1 Report: Trash Collector Bot

## Progress So Far
- Completed hardware procurement.
- Completed assembling the robot kit.
- Configured Raspberry Pi for automatic WiFi connection and SSH on boot via systemd service.
- Wrote scripts to take pictures in real time and deploy images to cloud/cnn locally
- Trained Yolo on images

## Goals - Modifications to Project Scope
Create a robot using machine learning for trash collection and real-time decisions. We're comparing a state machine and machine learning model for trash collection and adding a spatial localization and pathfinding system. The final goal is a robot that navigates an obstacle course, identifying obstacles and picking up trash, resembling an automated system for suburban areas.

## Course Topics
### FSM

![image](https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/174bcfe7-8111-407b-9c8c-0eb78aba4025)

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

### Jiamu's role is
- Write python scripts for tinyML and taking pictures.
- Finish training & finetuning Yolo-v5 and deploy the model
- Maintain the docs, and write the report for submission

### Samyak's role is
- Aiding in mechanical robot assembly.
- Implementing spatial localization and path finding (navigation) algorithm on robot.

### Hanson's role is 
- Assemble the power system, mechanical structure of the robot
- Set up system on microsd card 
- Merge the machine learning model with the robot's driving and arm functions


## Risks Identified
- **Crappy OS:** Rasp Pi OS has lots of problems, including cv2 problem, interface has no camera, python needs to be in env mode, crappy apt package manager. In comparision, Arch Linux is much better, with good package manager(pacman and aur), and high-level customization.
- **Controlling the Robot:** Crappy code from Adeept Bot online makes it hard to control the robot to do certain things with its claws and its wheels.
Besides the OS and controlling I don't think there will be any problems.

## Repositories
- GitHub: [EECS-149 Final Project Repository](https://github.com/jimchen2/EECS-149-Final-Project)
- Gitbook: [EECS-149 Final Project Docs](https://berkeley-7.gitbook.io/pro/)
