import time,sys
import RPi.GPIO as GPIO
import smbus
import led

def main():
    pulse= grove_fingerclip_heart_sensor()
    while True:
        time.sleep(2)
        try:
            pulse.pulse_read()
        except IOError:
            print("Error")
            led.apagar()

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

class grove_fingerclip_heart_sensor:
    address = 0x50

    def pulse_read(self):
        print(bus.read_byte(0x50))
        if bus.read_byte(0x50) > 85:
            led.encender()
            print("Carefull")
        else:
            led.apagar()
        # return bus.read_i2c_block_data(self.address, 1,1)

if __name__ == "__main__":
    main()
    