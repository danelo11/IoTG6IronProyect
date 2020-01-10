#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import led


channel = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
    
def callbackdet(channel):
    print("flame detected")
    led.encender()
    time.sleep(.5)
    led.apagar()
    
GPIO.add_event_detect(channel, GPIO.BOTH,bouncetime=300)
GPIO.add_event_callback(channel, callbackdet)
          
while True: 
    time.sleep(1)
    
    
        
   
    