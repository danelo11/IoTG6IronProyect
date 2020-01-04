Sensores
----------------------------------------------------------------
Flame sensor 1.1 D5
Temperature and humidity 1.2 D16
Gas sensor 1.5 
Led Socket kit 1.5
----------------------------------------------------------------
Flame sensor 1.1 D5
codigo:

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
--------------------------------------------------------------------
Temperature and humidity 1.2 D16

import time
import seeed_dht
def main():

    
    sensor = seeed_dht.DHT("16")

    while True:
        humi, temp = sensor.read()
        if not humi is None:
            print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensor.dht_type, humi, temp))
        else:
            print('DHT{0}, humidity & temperature: {1}'.format(sensor.dht_type, temp))
        time.sleep(1)


if __name__ == '__main__':
    main()
 
-----------------------------------------------------------------------
Gas sensor 1.5 A0
import math
import sys
import time
from grove.adc import ADC


class GroveGasSensorMQ5:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def MQ5(self):
        value = self.adc.read(self.channel)
        return value

Grove = GroveGasSensorMQ5


def main():
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = GroveGasSensorMQ5(int(sys.argv[1]))

    print('Detecting...')
    while True:
        print('Gas value: {0}'.format(sensor.MQ5))
        time.sleep(.3)

if __name__ == '__main__':
    main()
------------------------------------------------------------------------
Led Socket kit 1.5 D18

# GrovePi LED Blink example

import time
from grovepi import *

# Connect the Grove LED to digital port D4
led = 18

pinMode(led,"OUTPUT")
time.sleep(1)

while True:
    try:
        #Blink the LED
        digitalWrite(led,1)     # Send HIGH to switch on LED
        time.sleep(1)

        digitalWrite(led,0)     # Send LOW to switch off LED
        time.sleep(1)

    except KeyboardInterrupt:   # Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:             # Print "Error" if communication error encountered
        print "Error"



