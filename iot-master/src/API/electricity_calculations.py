import datetime
from datetime import timedelta, date, time

import numpy
import numpy as np
# returns lists of water usage calculations for each day jan 1 - april 30

dates = []
string_dates = []

shower_gal = []
bath_gal = []
shower_hot_gal = []
bath_hot_gal = []

dishes_gal = []
dishes_hot_gal = []
laundry_gal = []
laundry_hot_gal = []

shower_strings = []
bath_strings = []

dishes_strings = []
laundry_strings = []

class ElectricityCalculator:
    # Return values will be return kilowatts * usage time(hours), returns kWh
    def __init__(self):
        self.electricityPrice=0.12

    def cost(self, kWh):
        return self.electricityPrice*kWh

    def microwave(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 1.1*(20/60)
        else:
            return 1.1*0.5

    def stove(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 3.5*0.25
        else:
            return 3.5*0.5

    def oven(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 4*0.75
        else:
            return 4

    def livingRoomTV(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 0.636*4
        else:
            return 0.636*8

    def bedroomTV(self, dt):
        if dt.weekday()<=4: # Monday=0, Friday=4
            return 0.1*2
        else:
            return 0.1*4

    def dishwasher(self, dt, loads):
        return 1.8*0.75*loads

    def clothesWasher(self, dt, loads):
        return 0.5*0.5*loads

    def clothesDryer(self, dt):
        return 3*0.5*loads

    def fridge(self, dt):
        return 0.15*24

    def lightBulb(self, dt):
        return 0.06*24 # Placeholder until I know how long lightbulbs are used for

    def bathExhaust(self, dt):
        return 0.03*24 # Same as lightbolb

    def hotWaterHeater(self, dt, gal):
        return 4.5*(4/60)*gal

    def hvac(self, dt): # hvac is a bit of a toughie to figure out
        def operationUsage(hours):
            return 3.5*hours
        pass


def daterange():
    start_dt = date(2021, 1, 1)  # jan 1st
    end_dt = date(2021, 4, 30)  # april 30th

    for n in range(int((end_dt - start_dt).days)+1):
        yield start_dt + timedelta(n)


def create_dates():
    for dt in daterange():
        date = dt  # date objects to use in calculating weekdays
        string_date = dt.strftime("%Y-%m-%d")  # string of dates to use in final list
        dates.append(date)
        string_dates.append(string_date)
    return dates, string_dates

def calculate_eletricity_usage():
    ec=ElectricityCalculator()
    dailyElectricityCosts=[]
    for dt in daterange():
        pass #Have to figure out how I'll be getting the hot gallons used before I can even start calculating



    # Not sure how all this works, so not deleting it just yet
    # total_gallons = [a + b + c + d for a, b, c, d in zip(shower_gal, bath_gal, dishes_gal, laundry_gal)]
    # total_gallons_daily = [list(e) for e in zip(string_dates, total_gallons)]
    #
    # total_hot = [w + x + y + z for w, x, y, z in zip(shower_hot_gal, bath_hot_gal, dishes_hot_gal, laundry_hot_gal)]  # gives total gallons of hot water used
    # total_hot_daily = [list(e) for e in zip(string_dates, total_hot)]
    #
    # total_water_records =  [tuple(e) for e in zip (string_dates, total_gallons, total_hot)]

    #Note From Will: You can get rid of the lines below if you want, this is just for my testing/thinking purposes.
    print("\n.....................................................................................")
    print(f"Timestamp of this run: {datetime.datetime.now()}")
    print("\n.....................................................................................")
    print("\n")
    
    print("TODO (if needed) include some sort of diagnostic print stuff to test calculate_electricity_usage()")
