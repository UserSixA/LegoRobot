# Motor.py
from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Constants
DRIVE_SPEED = 200

ROTATE_SPEED = 100
ROTATE_ANGLE = 95

LIFT_SPEED = 300
LIFT_ANGLE = -50

GRAB_SPEED = 800
GRABBER_ANGLE = 850

class Motors:
    def __init__(self):
        self.grabber_motor = Motor(Port.D)
        self.drive_motor = Motor(Port.C)
        self.lift_motor = Motor(Port.B)
        self.rotate_motor = Motor(Port.A)
        self.gyro_sensor = GyroSensor(Port.S4)
        self.gyro_sensor.reset_angle(0)


    # === Lift Control ===
    def lift_up(self):
        self.lift_motor.run_angle(LIFT_SPEED, LIFT_ANGLE, then=Stop.HOLD, wait=True)
        wait(500)
        #self.lift_motor.run_angle(LIFT_SPEED, LIFT_ANGLE, then=Stop.HOLD, wait=True)

    def lift_down(self):
        self.lift_motor.run_angle(LIFT_SPEED, LIFT_ANGLE)
    
    def lift_drop(self):
        self.lift_motor.stop()


    # === Grabber Control ===
    def grabber_close(self):
        self.grabber_motor.run_angle(GRAB_SPEED, 4 * -GRABBER_ANGLE)

    def grabber_open(self):
        self.grabber_motor.run_angle(GRAB_SPEED, 4 * GRABBER_ANGLE)
        self.grabber_motor.stop()


    # === Drive Control ===
    def drive_backward(self):
        self.drive_motor.run(DRIVE_SPEED)

    def drive_forward(self):
        self.drive_motor.run(-DRIVE_SPEED)

    def stop_driving(self):
        self.drive_motor.stop()


    # === Rotate Control ===
    def rotate_left(self):
        self.rotate_motor.run_angle(ROTATE_SPEED, ROTATE_ANGLE, then=Stop.HOLD, wait=True)
        wait(500)

    def rotate_right(self):
        self.rotate_motor.run_angle(-ROTATE_SPEED, ROTATE_ANGLE, then=Stop.HOLD, wait=True)
        wait(500)