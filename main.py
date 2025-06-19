#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from Sensor import Sensors
from Motor import Motors

ev3 = EV3Brick()
sensors = Sensors()
motors = Motors()
""" 
##### TEST-FAHRT
#motors.lift_up()
#motors.rotate_right()
motors.drive_backward()
wait(1000)
motors.drive_forward()
wait(1000)
motors.stop_driving()
#ev3.speaker.say("Ben")
 """


######## Tischkante abfahren #######  FUNKTIONIERT GETESTET
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


### GREIFER HEBEN VOM BODEN
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



###### QUALIFIKATIONS-TEST  ### FEHLGESCHLAGEN
""" print("START")
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
ev3.speaker.say("Ben") """




######## Tournament Program (Stacking blocks) ####### FUNKTIONIERT GETESTET
first_color = 0
second_color = 0
second_color_done = False
#motors.grabber_close()
motors.lift_up()
#motors.grabber_open()
motors.drive_backward()
while (not sensors.back_edge_detected()): # Continue driving till either edge was detected or a third color was found
    color = sensors.get_color()
    if color != "Unkown":
        if(color == first_color):
            motors.stop_driving()
            motors.grabber_close()
            motors.lift_up()
            motors.rotate_left()
            motors.grabber_open()
            motors.lift_drop()
            wait(500)
            motors.lift_up()
            motors.rotate_right()
            motors.drive_backward()
        if(color == second_color) and (not second_color_done):
            motors.stop_driving()
            motors.grabber_close()
            motors.lift_up()
            motors.rotate_left()
            motors.rotate_left()
            motors.grabber_open()
            motors.lift_drop()
            wait(500)
            motors.lift_up()
            motors.rotate_right()
            motors.rotate_right()
            motors.drive_backward()
            second_color_done = True

        if(first_color == 0):   # Found a first color
            first_color = color
        elif(second_color == 0) and (first_color != 0):
            second_color = color

    # Print all color states
    ev3.screen.clear()
    ev3.screen.print("Current color : ", color)
    ev3.screen.print("First color   : ", first_color)
    print("Color      : ", color)
    print("First color   : ", first_color)
    print()
    wait(100)
motors.stop_driving()
ev3.speaker.say("DONE")



# Main loop
while True:
    
    # Display Sensor Values
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