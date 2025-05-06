# Motor.py
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Constants
DRIVE_SPEED = 400
TURN_SPEED = 400
LIFT_SPEED = 100
GRAB_SPEED = 800
LIFT_ANGLE = 40
LIFT_ANGLE_WEAK = 5
GRABBER_ANGLE = 360
TURN_ANGLE_90 = 510


class Motors:
    def __init__(self):
        self.right_motor = Motor(Port.D)
        self.grabber_motor = Motor(Port.C)
        self.lift_motor = Motor(Port.B)
        self.left_motor = Motor(Port.A)


    # === Lift Control ===
    def lift_init(self):
        self.lift_motor.run_angle(LIFT_SPEED, -22)

    def lift_weak_up(self):
        self.lift_motor.run_angle(LIFT_SPEED, -LIFT_ANGLE_WEAK)

    def lift_weak_down(self):
        self.lift_motor.run_angle(LIFT_SPEED, LIFT_ANGLE_WEAK)

    def lift_up(self):
        self.lift_motor.run_angle(LIFT_SPEED, -LIFT_ANGLE)

    def lift_down(self):
        self.lift_motor.run_angle(LIFT_SPEED, LIFT_ANGLE)
    
    def lift_drop(self):
        self.lift_motor.stop()

    # === Grabber Control ===
    def grabber_init(self):
        self.grabber_motor.run_angle(GRAB_SPEED, 5 * -GRABBER_ANGLE)
        self.grabber_motor.run_angle(GRAB_SPEED, 5 * GRABBER_ANGLE)

    def grabber_close(self):
        self.grabber_motor.run_angle(GRAB_SPEED, 4 * -GRABBER_ANGLE)

    def grabber_open(self):
        self.grabber_motor.run_angle(GRAB_SPEED, 4 * GRABBER_ANGLE)
        self.grabber_motor.stop()

    # === Drive Control ===
    def drive_backward(self):
        self.left_motor.run(DRIVE_SPEED)
        self.right_motor.run(DRIVE_SPEED)

    def drive_forward(self):
        self.left_motor.run(-DRIVE_SPEED)
        self.right_motor.run(-DRIVE_SPEED)

    def drive_forward_left(self):
        self.left_motor.run(-DRIVE_SPEED)
        self.right_motor.run(-DRIVE_SPEED * 0.95)

    def stop_driving(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def turn_left(self):
        self.left_motor.run(TURN_SPEED)
        self.right_motor.run(-TURN_SPEED)

    def turn_right(self):
        self.left_motor.run(-TURN_SPEED)
        self.right_motor.run(TURN_SPEED)

    def turn_left_90(self):
        self.left_motor.run_angle(-TURN_SPEED, TURN_ANGLE_90, wait=False)
        self.right_motor.run_angle(TURN_SPEED, TURN_ANGLE_90)

    def turn_right_90(self):
        self.left_motor.run_angle(TURN_SPEED, TURN_ANGLE_90, wait=False)
        self.right_motor.run_angle(-TURN_SPEED, TURN_ANGLE_90)