from move import setup, motor_left, motorStop, destroy

if __name__ == '__main__':
    try:
        speed = 60  # Define your speed
        setup()
        motor_left(1, 0, speed)  # Move left
        # Add a time delay if required
        motorStop()
        destroy()
    except KeyboardInterrupt:
        destroy()
