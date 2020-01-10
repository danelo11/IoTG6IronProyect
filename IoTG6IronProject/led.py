import time
import RPi.GPIO as GPIO

# Connect the Grove LED to digital port D18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

def encender():
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1) 

def apagar():
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)
    