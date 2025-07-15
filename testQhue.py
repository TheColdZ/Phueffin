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

    while True :
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'}
        r = requests.get(API_ADDRESS, headers = headers)
        print( r.status_code)
        print("\n planedloads\n", r.json()[0]['plannedLoads'][:10])
        next10TrashPickups = r.json()[0]['plannedLoads'][:10]

        trashPickupsTodayOrTomorrow = get_trash_pickups_today_or_tomorrow(next10TrashPickups)
        if (trashPickupsTodayOrTomorrow):
            print("light 2", lights(2)['state']['on'])
            while True:
                #Add additional conditioning here, i.e. if light source status has changed since the while loop started (i.e. people have stopped the blinking)

                if light_should_activate():
                    #activate_light
                    lights(2, 'state', on = True)
                    time.sleep(4)
                    lights(2, 'state', on = False)
                    time.sleep(2)
                #We get it, we need to take the bins out.... leave me alone. 
                if lights(2)['state']['on']:
                    print("Alright, taking a break, but don't forget to put the bins out!!!")
                    time.sleep(14400) #Sleep for 4 hours to get outside window of check, hardcoded it is...
                    break
                #The pickups are no longer today or tomorrow
                if not get_trash_pickups_today_or_tomorrow(trashPickupsTodayOrTomorrow):
                    break
        #Check every 15 minutes
        time.sleep(900)


def get_trash_pickups_today_or_tomorrow(trashPickups):
    return [pickup for pickup in trashPickups if date_is_today_or_tomorrow(datetime.fromisoformat(pickup['date']))]
    
def date_is_today_or_tomorrow(dateToCheck):
    return date_is_today(dateToCheck) or date_is_tomorrow(dateToCheck)

def date_is_tomorrow(dateToCheck):
    tomorrow = datetime.now() + timedelta(hours = 24)
    print("tomorrow", tomorrow)
    is_tomorrow = dateToCheck.date() == tomorrow.date()
    print("is_tomorrow", is_tomorrow)
    return is_tomorrow 

def date_is_today(dateToCheck):
    return dateToCheck.date() == datetime.now().date()

def light_should_activate():
    now = datetime.now()
    #Very hardcoded for now, as everything else... eventally create some smart comparison function that can take some input from env var/similar
    today20pm = now.replace(hour=20, minute=0, second=0, microsecond=0)
    today23pm = now.replace(hour=23, minute=0, second=0, microsecond=0)
    today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
    today9_30am = now.replace(hour=9, minute=30, second=0, microsecond=0)

    return ( now > today20pm and now < today23pm ) or ( now > today8am and now < today9_30am)


if __name__ == "__main__":
    main()