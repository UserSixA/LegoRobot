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
#motors.lift_init()
#motors.grabber_init()



##### JETZT
#motors.lift_up()
#motors.rotate_right()
""" motors.drive_backward()
wait(1000)
motors.drive_forward()
wait(1000)
motors.stop_driving() """
#ev3.speaker.say("Ben")



######## Tischkante #######  FUNKTIONIERT GETESTET
""" motors.drive_backward()
while not sensors.back_edge_detected():
    print("still driving backwards")
motors.drive_forward()
while not sensors.front_edge_detected():
    print("still driving forwards")
motors.stop_driving()
ev3.speaker.say("Ben") """


######## Blöcke erkennen ####### FUNKTIONIERT GETESTET
""" first_color = 0
second_color = 0
false_color = False

motors.lift_up()

motors.drive_backward()
while (not sensors.back_edge_detected()) and (not false_color):
    color = sensors.get_color()
    if color != "Unkown":
        if(first_color == 0):
            first_color = color
        elif(second_color == 0) and (color != first_color):
            second_color = color
        if(first_color != 0) and (second_color != 0) and (color != first_color) and (color != second_color):
            false_color = True


    ev3.screen.clear()
    ev3.screen.print("Current color : ", color)
    ev3.screen.print("First color   : ", first_color)
    ev3.screen.print("Second color  : ", second_color)
    ev3.screen.print("False color   :", false_color)
    print("Color      : ", color)
    print("First color   : ", first_color)
    print("Second color  : ", second_color)
    print("False color   :", false_color)
    print()
    wait(100)
motors.stop_driving()
print("There was a false color: ", false_color)
ev3.speaker.say("Ben") """




### GREIFEN HEBEN VOM BODEN
""" #motors.grabber_open()
motors.lift_up()
motors.grabber_close()
motors.lift_up()
#motors.rotate_left()
motors.drive_backward()
wait(2000)
motors.stop_driving()
#motors.lift_down()
#motors.grabber_open() """



###### BUSSING
print("START")

#motors.grabber_open()
motors.lift_up()
motors.drive_backward()
color = sensors.get_color()
while (not sensors.back_edge_detected()) and (color != "Blue"):
    color = sensors.get_color()
    print("Still driving...")
print("Found Block!")
wait(100)
motors.stop_driving()
motors.grabber_close()
motors.lift_up()
motors.rotate_right()
motors.lift_drop()
motors.grabber_open()
ev3.speaker.say("Ben")



#ev3.speaker.say("Robot started")




# FIND WALL - ACTION
""" motors.drive_forward()
if(sensors.edge_detected()) motors.turn_right_90() """


# BLOCK DETECTION - ACTION
""" motors.lift_up()
motors.turn_right_90()
motors.lift_drop()
motors.lift_weak_up()
ev3.speaker.say(sensors.get_color())
motors.lift_weak_up()
motors.grabber_close()
motors.lift_weak_up()
motors.turn_left_90()
motors.lift_down() """
""" motors.lift_weak_down()

wait(1000)
motors.turn_left()
wait(1000)
motors.drive_backward()
wait(1000) """

#motors.turn_left_90()
#wait(4000)




#motors.grabber_init()
#motors.grabber_open()
#wait(1000)


""" motors.grabber_close()
motors.lift_up() """


#motors.grabber_open()

#Begining
""" motors.lift_up()
motors.drive_backward()
while(sensors.get_ultrasonic_distance() > 100):
    print("still driving")
wait(190)
motors.stop_driving()
motors.grabber_close()
motors.lift_up()
wait(300)

distance = sensors.get_ultrasonic_distance()
if(sensors.holds_block()):
    ev3.screen.print("Found block")
    ev3.screen.print("distance: ", distance)
    motors.drive_forward()
    wait(1800)
    motors.stop_driving()
    motors.lift_down()
    motors.lift_drop()
    wait(1000)
    motors.grabber_open()

    motors.grabber_open()
    motors.lift_up()
    motors.grabber_close()
    motors.lift_up()
else:
    ev3.screen.print("No block")
    ev3.screen.print("distance: ", distance) """





""" wait(10000)

motors.lift_down()
motors.grabber_open() """


# Main loop
while True:
    

    color = sensors.get_color()
    us_dist = sensors.get_ultrasonic_distance()
    ir_dist = sensors.get_infrared_distance()

    ev3.screen.clear()
    ev3.screen.print("US distance: ", us_dist)
    ev3.screen.print("IR distance: ", ir_dist)
    ev3.screen.print("Color      : ", color)

    print("US distance: ", us_dist)
    print("IR distance: ", ir_dist)
    print("Color      : ", color)
    print()
    wait(200)




    """ touched = sensors.is_touched()
    us_dist = sensors.get_ultrasonic_distance()
    ir_dist = sensors.get_infrared_distance()
    edge_detected = sensors.edge_detected()
    block_detected = sensors.block_detected() """

    # Display on EV3
    #ev3.screen.clear()
    #ev3.screen.print("Color:      ", color)
    """ ev3.screen.print("Touch:      ", "Yes" if touched else "No")
    ev3.screen.print("Ultrasonic: ", us_dist, "mm")
    ev3.screen.print("Infrared:   ", ir_dist)
    ev3.screen.print("Edge Det.:  ", edge_detected)
    ev3.screen.print("Block Det.: ", block_detected) """

    #print("Color: ", color)
    """ print("Touch: ", touched)
    print("Ultrasonic: ", us_dist, "mm")
    print("Infrared: ", ir_dist)
    print("Edge detected: ", edge_detected)
    print("Block detected: ", block_detected)
    print("State: ", state)
    print("----------------------") """


     # --- State Machine ---
    """ if state == FIND_WALL:
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
            state = FIND_WALL

    wait(500)
 """


