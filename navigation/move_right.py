from move import setup, motor_right, motorStop, destroy

if __name__ == '__main__':
    try:
        speed = 60  # Define your speed
        setup()
        motor_right(1, 0, speed)  # Move right
        # Add a time delay if required
        motorStop()
        destroy()
    except KeyboardInterrupt:
        destroy()
