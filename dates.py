import pandas as pd
import datetime

start = datetime.datetime(1000, 8, 15)
end = datetime.datetime(2000, 7, 15)

start2 = datetime.datetime(2021, 4, 26)
end2 = start2 + (end-start)

def shiftDate(date, days):
    return date + datetime.timedelta(days=days)

def shiftDateBack(date, days):
    return date - datetime.timedelta(days=days)

delta = (start2 - start).days
date = datetime.datetime.today()

print (shiftDate(end, delta).strftime("%B %d, %Y"))
print (shiftDateBack(datetime.datetime.today(), delta).strftime("%B %d, %Y"))
