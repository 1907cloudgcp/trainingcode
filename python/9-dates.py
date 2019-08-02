#!/usr/bin/env python3

'''
Dates

Includes: Datetime, Timedeltas, Timestamp, Date manipulation

-> They are big numbers behind the scenes
-> This means that you can substract them and add them together, or any math operation
-> Dates can be *Aware* of a timezone, or *Naive* of them.

We will focus on Naive formatting
'''

from datetime import datetime, timedelta
from time import time

def main():
    #One Day representation delta
    day = timedelta(days=1)

    #Timestamp representation (use for precise computing time)
    #Number of ticks since 12:00am, January 1, 1970
    timestamp = time()
    print('Number of ticks: ' + str(timestamp))

    #You could also get today's date using
    print('Today is: ' + str(datetime.now()))

    #Calculate your first payday 
    first_work_day = datetime.fromtimestamp(timestamp)
    first_pay_day = datetime(year=2019, month=2, day=27, hour=17, minute=0, second=0, microsecond=0)
    delta_to_first_pay = first_pay_day - first_work_day

    #Additions will return a new datetime with the added delta
    print('Tomorrow is: ' + str(first_work_day + day))

    #Substractions return a timedelta which you can use to extract a specific parameter of time
    print('You will get first check in: ' + str(delta_to_first_pay.days) + ' days.')
    
if __name__ == '__main__':
    main()