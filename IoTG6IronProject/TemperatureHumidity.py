#! /usr/bin/python3
import time
import seeed_dht
import argparse
import requests
import led

URL = 'https://corlysis.com:8086/write'
READING_DATA_PERIOD_MS = 1000.0
SENDING_PERIOD = 2
MAX_LINES_HISTORY = 1000

def main():
    temphumi()
    
def temphumi():
    parser = argparse.ArgumentParser()
    parser.add_argument("db", help="database name")
    parser.add_argument("token", help="secret token")
    args = parser.parse_args()
    corlysis_params = {"db": args.db, "u": "token", "p": args.token, "precision": "ms"}
    payload = ""
    counter = 1
    problem_counter = 0
    sensor = seeed_dht.DHT("11",22)
    i = 1
    while i <=10:
        unix_time_ms = int(time.time()*1000)
        dataset = sensor.read()
        humi = dataset[0]
        temp = dataset[1]
        init = "temp_humi,temp="
        cont = "humidity="
        if humi >= 65 or temp >= 25:
            if humi >= 65:
                print("Es lo que tiene Bilbao")
                led.encender()
            if temp >= 25:
                print("Para ser invierno esta bien")
                led.encender()
        else:
            led.apagar()
            
        if not humi is None:
            print('humidity {1:.1f}% temperature {2:.1f}ºC'.format(sensor.dht_type, humi, temp, unix_time_ms))
            line = "{}{} {}{}".format(init,str(temp),cont,str(humi))
            payload += line
            print (payload)
            i = i+1
            time.sleep(1.5)
        else:
            print('humidity & temperature: {1}'.format(sensor.dht_type,humi, temp, unix_time_ms))
        if counter % SENDING_PERIOD == 0 or counter % SENDING_PERIOD != 0:
            try:
                r = requests.post(URL, params=corlysis_params, data=payload)
                payload = ""
                if r.status_code == 204:
                    print("HTTP/1.1 204")
                if r.status_code != 204:
                    raise Exception("data not written")
            except:
                problem_counter += 1
                if problem_counter == MAX_LINES_HISTORY:
                    problem_counter = 0
                    payload = ""
        counter += 1
        time_diff_ms = int(time.time()*1000) - unix_time_ms
        if time_diff_ms < READING_DATA_PERIOD_MS:
            time.sleep((READING_DATA_PERIOD_MS - time_diff_ms)/1000.0)
          
if __name__ == '__main__':
    main()
    

    

