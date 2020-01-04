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