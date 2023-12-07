import trash_collector
import recognizeline
import time
import sys
sys.path.append('/home/pi/Adeept_RaspTank/server')  # Add the directory containing 'move.py' to the Python path

from move import setup, motor_left,motor_right, motorStop, destroy,move  # Now you can import normally

MID_POSITION =  # Define the mid-position value

def main():
    while True:
        if recognizeline.detect_line():
            follow_line()
        else:
            go_forward()

        if trash_collector.see_tin_can():
            pick_up_trash()

        time.sleep(0.1)

def pick_up_trash():
    while trash_collector.trash_position() != MID_POSITION:
        adjust_motor_for_trash()

    trash_collector.pick_up_trash()

def adjust_motor_for_trash():
    # Logic to adjust motor so that the trash is in the middle position
    pass

def follow_line():
    # Adjust motor speed to follow the line
    pass

def go_forward():
    speed = 60  # Define your speed
    setup()
    motor_left(1, 0, speed)  # Move forward
    motor_right(1, 0, speed)

def go_backward():
    speed = 60  # Define your speed
    setup()
    motor_left(1, 1, speed)  # Move backward
    motor_right(1, 1, speed)


if __name__ == "__main__":
    main()
