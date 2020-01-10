#! /usr/bin/python3
import math
import sys
import time
from grove.adc import ADC
"""import argparse
import requests"""
import led

"""URL = 'https://corlysis.com:8086/write'
READING_DATA_PERIOD_MS = 1000.0
SENDING_PERIOD = 2
MAX_LINES_HISTORY = 1000"""

class GroveGasSensorMQ2:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()
    @property
    def MQ2(self):
        value = self.adc.read(self.channel)
        return value
    
Grove = GroveGasSensorMQ2

def main():
    """parser = argparse.ArgumentParser()
    parser.add_argument("db", help="database name")
    parser.add_argument("token", help="secret token")
    args = parser.parse_args()
    corlysis_params = {"db": args.db, "u": "token", "p": args.token, "precision": "ms"}
    payload = ""
    counter = 1
    problem_counter = 0"""
    g = 0
    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = GroveGasSensorMQ2(int(sys.argv[1]))

    print('Detecting...')

    while g<=10:
        """unix_time_ms = int(time.time()*1000)"""
        if sensor.MQ2 >= 55:
            led.encender()
        else:
            led.apagar()
        print('Gas value: {0}'.format(sensor.MQ2))
        g = g+1
        time.sleep(1.5)     
         
if __name__ == '__main__':
    main()