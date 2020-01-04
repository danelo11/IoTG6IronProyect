#!/usr/bin/env python
#

import time	
import grovepi

# Connect the Grove Flame Sensor to digital port D5
# SIG,NC,VCC,GND
flame_sensor = 5

grovepi.pinMode(flame_sensor,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(flame_sensor))
        time.sleep(.5)

    except IOError:
        print ("Error")