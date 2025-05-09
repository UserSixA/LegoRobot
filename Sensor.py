from pybricks.ev3devices import ColorSensor, UltrasonicSensor, InfraredSensor
from pybricks.parameters import Port

BLOCK_DETECTION_THRESHOLD = 5
EDGE_DETECTION_THRESHOLD = 50

class Sensors:
    def __init__(self):
        self.color_sensor = ColorSensor(Port.S2)
        self.ultrasonic_sensor = UltrasonicSensor(Port.S4)
        self.infrared_sensor = InfraredSensor(Port.S3)

    def get_color(self):
        r, g, b = self.color_sensor.rgb()
        reflection = self.color_sensor.reflection()

        # Avoid divide-by-zero
        total = r + g + b if (r + g + b) != 0 else 1

        # Normalize
        r_n = r / total
        g_n = g / total
        b_n = b / total

        # Print raw and normalized values
        print("r: ", r, " - g: ", g, " - b: ", b)
        print("r_norm: ", round(r_n, 2), " - g_norm: ", round(g_n, 2), " - b_norm: ", round(b_n, 2))

        # Calibrated simple thresholds — tweak these for your lighting
        if r + g + b < 15 and reflection > 1:
            return "Black"
        elif r_n > 0.4 and g_n < 0.3 and b_n < 0.3:
            return "Red"
        elif g_n > 0.4 and r_n < 0.3 and b_n < 0.3:
            return "Green"
        elif b_n > 0.4 and r_n < 0.3 and g_n < 0.4:
            return "Blue"
        elif r_n > 0.3 and g_n > 0.3 and b_n < 0.2:
            return "Yellow"
        elif r_n > 0.25 and g_n > 0.33 and b_n > 0.33:
            return "White"
        else:
            return "Unknown"

    def is_touched(self):
        return self.touch_sensor.pressed()

    def get_ultrasonic_distance(self):
        return self.ultrasonic_sensor.distance()

    def get_infrared_distance(self):
        return self.infrared_sensor.distance()
 
    def edge_detected(self):
        distance = self.ultrasonic_sensor.distance()
        return EDGE_DETECTION_THRESHOLD < distance < 2000

    def block_detected(self):
        distance = self.infrared_sensor.distance()
        return distance < BLOCK_DETECTION_THRESHOLD

    def holds_block(self):
        distance = self.get_ultrasonic_distance()
        return distance < 7
