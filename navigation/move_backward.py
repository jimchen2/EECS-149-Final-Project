from move import setup, motor_left, motor_right, motorStop, destroy

if __name__ == '__main__':
    try:
        speed = 60  # Define your speed
        setup()
        motor_left(1, 1, speed)  # Move backward
        motor_right(1, 1, speed)
        # Add a time delay if required
        motorStop()
        destroy()
    except KeyboardInterrupt:
        destroy()
