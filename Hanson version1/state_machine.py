import detect_line
import move
speed_set = 100
kp=0.1
def PID_function(input):
    return kp*input

class RobotStateMachine:
    def __init__(self):
        # Start in the Navigation Mode state
        self.state = "Navigation Mode"
        move.setup()

    # Define a method for each state in the state diagram

    def navigation_mode(self):
        # Implement navigation logic here
        print("Robot is in Navigation Mode, searching for trash or avoiding obstacles.")
        # Check sensors and switch state based on conditions
        if self.detect_trash():
            self.state = "Trash Picking Mode"
        elif self.detect_error():
            self.state = "Error Handling"
        line_position=detect_line.main()
        motor_input=PID_function(line_position-0.5)
        move.move(speed_set,'forward','precise',motor_input)
        # ... more conditions based on your state diagram

    # def error_handling(self):
    #     # Implement error handling logic here
    #     print("Robot is handling an error.")
    #     # Once the error is resolved, return to Navigation Mode
    #     self.state = "Navigation Mode"

    def trash_picking_mode(self):
        # Implement trash detection and picking logic here
        print("Robot is in Trash Picking Mode, trying to pick up trash.")
        # Once trash is centered, switch to Picking Up Mode
        self.state = "Picking Up Mode"

    # def picking_up_mode(self):
    #     # Implement picking up trash logic here
    #     print("Robot is picking up trash.")
    #     # Once trash is collected, check for more trash or return to Navigation Mode
    #     if self.more_trash_detected():
    #         self.state = "Trash Picking Mode"
    #     else:
    #         self.state = "Navigation Mode"

    # Define methods to simulate sensor input for demonstration purposes

    def detect_trash(self):
        # Simulate trash detection
        return False

    def detect_error(self):
        # Simulate error detection
        return False

    # Main loop to run the state machine
    def run(self):
        while True:
            # Call the method corresponding to the current state
            getattr(self, self.state.lower().replace(" ", "_"))()
            # Break the loop after one cycle for demonstration purposes

# Instantiate and run the state machine
robot = RobotStateMachine()
robot.run()