#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from Sensor import Sensors
from Motor import Motors

ev3 = EV3Brick()
sensors = Sensors()
motors = Motors()

# States
FIND_WALL = 1
DRIVE_TO_WALL = 2
FIND_BRICK = 3
PICK_UP_BRICK = 4
FIND_CLIFF = 5
PLACE_BLOCK = 6
RETURN_TO_WALL = 7
state = FIND_WALL

#motors.grabber_close()

# INIT
motors.lift_init()
motors.grabber_init()

# FIND WALL - ACTION
motors.drive_forward()
if(sensors.edge_detected()) motors.turn_right_90()


# BLOCK DETECTION - ACTION
motors.lift_up()
motors.turn_right_90()
motors.lift_drop()
motors.lift_weak_up()
ev3.speaker.say(sensors.get_color())
motors.lift_weak_up()
motors.grabber_close()
motors.lift_weak_up()
motors.turn_left_90()
motors.lift_down()
motors.lift_weak_down()


wait(1000)
motors.turn_left()
wait(1000)
motors.drive_backward()
wait(1000)

# Test1
# Test3

#motors.turn_left_90()
#wait(4000)


# Main loop
while True:
    color = sensors.get_color()
    """ touched = sensors.is_touched()
    us_dist = sensors.get_ultrasonic_distance()
    ir_dist = sensors.get_infrared_distance()
    edge_detected = sensors.edge_detected()
    block_detected = sensors.block_detected() """

    # Display on EV3
    ev3.screen.clear()
    ev3.screen.print("Color:      ", color)
    """ ev3.screen.print("Touch:      ", "Yes" if touched else "No")
    ev3.screen.print("Ultrasonic: ", us_dist, "mm")
    ev3.screen.print("Infrared:   ", ir_dist)
    ev3.screen.print("Edge Det.:  ", edge_detected)
    ev3.screen.print("Block Det.: ", block_detected) """

    print("Color: ", color)
    """ print("Touch: ", touched)
    print("Ultrasonic: ", us_dist, "mm")
    print("Infrared: ", ir_dist)
    print("Edge detected: ", edge_detected)
    print("Block detected: ", block_detected)
    print("State: ", state)
    print("----------------------") """


    """  # --- State Machine ---
    if state == FIND_WALL:
        motors.drive_forward()
        if touched:  # Touch sensor used to detect wall
            motors.stop_driving()
            state = FIND_BRICK

    elif state == FIND_BRICK:
        motors.turn_left()
        wait(1000)
        motors.stop_driving()
        if block_detected:
            state = PICK_UP_BRICK

    elif state == PICK_UP_BRICK:
        motors.lift_down()
        motors.grabber_close()
        wait(500)
        motors.lift_up()
        state = FIND_CLIFF

    elif state == FIND_CLIFF:
        motors.drive_forward()
        if edge_detected:
            motors.stop_driving()
            state = PLACE_BLOCK

    elif state == PLACE_BLOCK:
        motors.lift_down()
        motors.grabber_open()
        wait(500)
        motors.lift_up()
        state = RETURN_TO_WALL

    elif state == RETURN_TO_WALL:
        motors.drive_backward()
        if touched:
            motors.stop_driving()
            state = FIND_WALL """

    wait(500)



