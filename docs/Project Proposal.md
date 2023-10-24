# Project Proposal: Trash Collector Bot

**Team:** [Jiamu Chen](https://jimchen.me), [Samyak Tiwari](https://github.com/tiwar081), [Hanson Li](https://github.com/Hanson-Li-lchanggle), [Robert Lee](https://github.com/depetrol)

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
4. TinyML (TinyML is a branch of machine learning and embedded systems research that focuses on running low-power model inference on small devices like microcontrollers)

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
2. Integrate the picking up mechanism with Image Processing (we are still figuring out whether to use state machine or machine learning)

## Resources

**Hardware:**

| **Item**                                     | **Details**                                    |
|----------------------------------------------|------------------------------------------------|
| [Raspberry Pi 4 Model B CanaKit](https://www.amazon.com/dp/B08956GVXN?psc=1&ref=ppx_yo2ov_dt_b_product_details)   | Ordered by J. C. Total Price: $176.39         |
| [Camera Module V2-8 Megapixel, 1080p](https://www.amazon.com/dp/B01ER2SKFS?psc=1&ref=ppx_yo2ov_dt_b_product_details)   | Ordered by J. C. Total Price: $27.24          |
| [L298N Motor Drive Controller Board](https://www.amazon.com/gp/product/B07ZT619TD/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1) | Ordered by J. C. Total Price: $18.73          |
| [VGE Battery Pack, 5000mAh, 5V 2.0A](https://www.amazon.com/dp/B09HXYTDMV?psc=1&ref=ppx_yo2ov_dt_b_product_details)   | Ordered by J. C. Total Price: $28.61          |
| [L293 IC Stepper Motor Drivers Controllers](https://www.amazon.com/dp/B07NXTWJV9?psc=1&ref=ppx_yo2ov_dt_b_product_details)    | Ordered by J. C. Total Price: $9.79           |
| [4PCS Breadboards Kit](https://www.amazon.com/dp/B07DL13RZH?psc=1&ref=ppx_yo2ov_dt_b_product_details)   | Ordered by J. C. Total Price: $11.00          |
| [Chanzon 120pcs Header Jumper Wire](https://www.amazon.com/dp/B09FPGT7JT?psc=1&ref=ppx_yo2ov_dt_b_product_details)  | Ordered by J. C. Total Price: $11.01          |
| [SUPULSE Lipo Charger](https://www.amazon.com/dp/B08L7VCBXG?psc=1&ref=ppx_yo2ov_dt_b_product_details)   | Ordered by J. C. Total Price: $22.04          |
| Proximity Sensors                            | --                                             |
| Trash Pickup Claw                            | --                                             |
| Vehicle frame                                | --                                             |

**Software:**

| **Software**     | **Purpose**                              |
|------------------|------------------------------------------|
| Raspberry Pi OS  | OS for Raspberry Pi                      |
| PyTorch          | For implementing CNN                     |
| ChatGPT          | For debugging, and formatting documents  |

