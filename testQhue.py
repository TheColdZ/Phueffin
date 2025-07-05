#Initial 'hacky' (it's extremely hacky, almost to embarassing to commit, but here we are) script for controlling hue lights. 

import json
from os import path
from qhue import Bridge
from datetime import datetime, timedelta
import requests
import time

# the IP address of your bridge
BRIDGE_IP = "192.168.0.207"

CRED_FILE_PATH = "hue_username.txt"

API_ADDRESS_PATH = "api_address.txt"
            

    #time_val = datetime.datetime.strptime(r.json()[0]['plannedLoads'][0]['date'], '%Y-%m-%dT%H:%M:%S.%f')
    #print(time_val)
def main():

    with open(CRED_FILE_PATH, "r") as cred_file:
            USER_NAME = cred_file.read()

    with open(API_ADDRESS_PATH, "r") as cred_file:
            API_ADDRESS = cred_file.read()

    # create the bridge resource, passing the captured username
    bridge = Bridge(BRIDGE_IP, USER_NAME)

    # create a lights resource
    lights = bridge.lights

    # query the API and print the results as JSON
    #print(json.dumps(lights(), indent=2))

    #while True :
    #    lights(2, 'state', on = True)
    #    time.sleep(4)
    #    lights(2, 'state', on = False)
    #    time.sleep(4)

    while True :
        time.sleep(1)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'}
        r = requests.get(API_ADDRESS, headers = headers)
        print( r.status_code)
        print(r.json()[0]['plannedLoads'][0]['date'])
        trash_collection_time = datetime.fromisoformat(r.json()[0]['plannedLoads'][0]['date'])
        print(trash_collection_time)
        checktime = datetime.now() + timedelta(hours = 72)
        print(checktime)
        trash_will_be_collected_tomorrow = trash_collection_time.date() == checktime.date()
        print("Trash", trash_will_be_collected_tomorrow)
        while trash_will_be_collected_tomorrow :
            lights(2, 'state', on = True)
            time.sleep(4)
            lights(2, 'state', on = False)
            time.sleep(2)
#Test, is this working? 

if __name__ == "__main__":
    main()