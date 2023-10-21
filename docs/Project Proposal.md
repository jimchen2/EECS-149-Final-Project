# Project Proposal: Trash Collector Bot

**Team:** Jiamu Chen [https://jimchen.me](https://jimchen.me)

## Goal

Design a robot that finds and picks up trash. It uses machine learning (image processing) and real-time interference to know trash from non-trash.

## How It Works

The robot learns to see trash with a machine learning system.

- **Camera:** to move around and spot trash.
  
- **Proximity Sensors:** To avoid obstacles and navigate.

## Course Topics Addressed

1. Sensors and Actuators
2. MBD & Modeling Physical Dynamics
3. Networking
4. TinyML

## Schedule

Work 3 hours in lab every week. Details to come later.

## Github Repo

[https://github.com/jimchen2/EECS-149-Final-Project](https://github.com/jimchen2/EECS-149-Final-Project)

## Risks

Making the robot learn efficiently can be hard. The budget may affect our choices. Making all parts work smoothly together might be tricky.

# Approach

## Project Initialization(done)

1. Acquire necessary hardware components.
2. Set Up Raspberry Pi OS

## Hardware Setup

1. Assemble Raspberry Pi, attach camera.
2. Connect sensors, Set up motors
3. Test moving around with motors

## Image Recognition

1. Acquire and preprocess trash image dataset.
2. Train a CNN for trash identification.
3. Export model to Raspberry Pi.

## Picking Up Trash

1. Integrate a claw on the Raspberry Pi.
2. Integrate the picking up mechanism with Image Processing

## Resources

**Hardware:**

| **Item**                                         | **Details**                                             |
|--------------------------------------------------|---------------------------------------------------------|
| Raspberry Pi 4 Model B CanaKit                   | Ordered by J. C. Total Price: $176.39                   |
| Camera Module V2-8 Megapixel, 1080p              | Ordered by J. C. Total Price: $27.24                    |
| L298N Motor Drive Controller Board               | Ordered by J. C. Total Price: $18.73                    |
| VGE Battery Pack, 5000mAh, 5V 2.0A               | Ordered by J. C. Total Price: $28.61                    |
| L293 IC Stepper Motor Drivers Controllers        | Ordered by J. C. Total Price: $9.79                     |
| 4PCS Breadboards Kit                             | Ordered by J. C. Total Price: $11.00                    |
| Chanzon 120pcs Header Jumper Wire                | Ordered by J. C. Total Price: $11.01                    |
| SUPULSE Lipo Charger                             | Ordered by J. C. Total Price: $22.04                    |
| Proximity Sensors                                | --                                                      |
| Trash Pickup Claw                                | --                                                      |
| Vehicle frame                                    | --                                                      |

**Software:**

| **Software**     | **Purpose**                              |
|------------------|------------------------------------------|
| Raspberry Pi OS  | OS for Raspberry Pi                      |
| PyTorch          | For implementing CNN                     |
| ChatGPT          | For debugging, and formatting documents  |

