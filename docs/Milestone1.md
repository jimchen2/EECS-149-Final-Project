# Milestone 1 Report: Trash Collector Bot

## Architecture Drawing
<img src="https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/1701d585-b64e-4b02-b794-619a87e5b2e3" width="50%" /><img src="https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/8f3853a2-5093-4ee4-b0ad-18dce67e88f7" width="50%" />

<img src="https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/dded059a-2898-419d-812e-aec7a14e06c8" width="50%" /><img src="https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/e8e9c12e-6b01-48c0-984a-1817ebaa7b67" width="50%" />

## Progress So Far
- Completed hardware procurement.
- Achieved 50% completion in assembling the robot kit.
- Configured Raspberry Pi for automatic WiFi connection and SSH on boot via systemd service.
- Tried out Yolo on images

## Goals - Modifications to Project Scope
The primary objective remains to create a trash-collecting robot using machine learning for image recognition and real-time decision-making. We are evaluating the potential of employing a state machine against a machine learning model for the trash collection mechanism, with further refinements underway. We are incorporating one thing more: a spatial localization and path find system. Having the robot navigate some sort of obstacle course (with simple, predictable obstacles for the robot to identify) while picking up trash along the way will be the final output of our project, intended to resemble some practical automated trash collection system to be used in suburban areas.

## Resources Acquired
- Raspberry Pi CanaKit
- Robot Car Kit (including a robotic arm)

## Schedule
11/8-14: Complete mechanical assembly of robotic car and arm, test operation.

11/15-21: Integrate and deploy the machine learning model with the robot's camera. Implement navigation.

11/22-28: Finetune the trash collection method, potentially modifying the robot design.

11/29-12/12: Conduct debugging and troubleshooting. Write report + prepare presentation.

### Jiamu's role is
- Set up operating system and make the robot drive and arm move from python code
- Finish training & finetuning Yolo-v5 and deploy the model
- Maintain the docs, design the slides, and write the report for submission

### Samyak's role is
- Aiding in mechanical robot assembly.
- Implementing spatial localization and path finding (navigation) algorithm on robot.
- Presentations, poster, and report (all members will make contributions to this, Samyak will bear more responsibility here to tailor to English-speaking course community).

### Hanson's role is 
- Bought the robot car kit
- Assemble the power system, mechanical structure of the robot
- Merge the machine learning model with the robot's driving and arm functions


## Risks Identified
- **Kit Assembly:** The assembly process is more complex than anticipated, requiring significant time investment.
- **Operating System Deployment:** The 7GB operating system size is substantial compared to standard images, posing challenges in debugging and implementation.
- **Motor Integration:** Achieving seamless motor integration has proven more challenging than initially thought.
- **Machine Learning Deployment:** Running a comprehensive ML model on Raspberry Pi in real-time may pose performance challenges due to hardware limitations.

## Repositories
- GitHub: [EECS-149 Final Project Repository](https://github.com/jimchen2/EECS-149-Final-Project)
- Gitbook: [EECS-149 Final Project Docs](https://berkeley-7.gitbook.io/pro/)
