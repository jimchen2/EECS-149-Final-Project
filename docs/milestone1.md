# Milestone 1 Report: Trash Collector Bot

## Architecture Drawing
![image](https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/1701d585-b64e-4b02-b794-619a87e5b2e3)
![image](https://github.com/jimchen2/EECS-149-Final-Project/assets/123833550/8f3853a2-5093-4ee4-b0ad-18dce67e88f7)

## Progress So Far
- Completed hardware procurement.
- Achieved 50% completion in assembling the robot kit.
- Configured Raspberry Pi for automatic WiFi connection and SSH on boot via systemd service.

## Goals - Modifications to Project Scope
The primary objective remains to create a trash-collecting robot using machine learning for image recognition and real-time decision-making. We are evaluating the potential of employing a state machine against a machine learning model for the trash collection mechanism, with further refinements underway.

## Resources Acquired
- Raspberry Pi CanaKit
- Robot Car Kit (including a robotic arm)

## Schedule
Tasks are scheduled on a weekly basis starting now:
- Operate the car and robotic arm.
- Integrate and deploy the machine learning model with the robot's camera.
- Implement and fine-tune the trash collection method, potentially modifying the robot design.
- Conduct debugging and troubleshooting.

## Risks Identified
- **Kit Assembly:** The assembly process is more complex than anticipated, requiring significant time investment.
- **Operating System Deployment:** The 7GB operating system size is substantial compared to standard images, posing challenges in debugging and implementation.
- **Motor Integration:** Achieving seamless motor integration has proven more challenging than initially thought.
- **Machine Learning Deployment:** Running a comprehensive ML model on Raspberry Pi in real-time may pose performance challenges due to hardware limitations.

## Repositories
- GitHub: [EECS-149 Final Project Repository](https://github.com/jimchen2/EECS-149-Final-Project)
- GitBook: [Project Documentation](https://berkeley-7.gitbook.io/pro)
