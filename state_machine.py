import detect_line
import yolov5_trash
import PID_function

class RobotStateMachine:
    def __init__(self):
        self.state = "Navigation Mode"

    def navigation_mode(self):
        print("Robot is in Navigation Mode.")
        if self.detect_trash():
            self.state = "Trash Picking Mode"
        elif self.detect_error():
            self.state = "Error Handling"
        else:
            line_position = detect_line.detect()
            motor_input = PID_function.calculate(line_position)
            self.motor_move(motor_input)

    def error_handling(self):
        print("Handling error.")
        # Implement actual error handling logic here
        self.state = "Navigation Mode"

    def trash_picking_mode(self):
        print("Robot is in Trash Picking Mode.")
        self.state = "Picking Up Mode"

    def picking_up_mode(self):
        print("Robot is picking up trash.")
        if self.more_trash_detected():
            self.state = "Trash Picking Mode"
        else:
            self.state = "Navigation Mode"

    def detect_trash(self):
        return yolov5_trash.detect()

    def detect_error(self):
        # Implement actual error detection logic
        return False

    def more_trash_detected(self):
        # Implement logic to detect more trash
        return False

    def motor_move(self, input):
        # Implement motor movement logic
        pass

    def run(self):
        while True:
            getattr(self, self.state.lower().replace(" ", "_"))()

robot = RobotStateMachine()
robot.run()
