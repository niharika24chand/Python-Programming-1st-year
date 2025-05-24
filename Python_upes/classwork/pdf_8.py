#To get current date and time using module named datetime
import datetime
datetime_object = datetime.datetime.now()    #We then used now() method to create a datetime object containing the current local date and time
print(datetime_object)

#To get current date
import datetime
date_object = datetime.date.today()
print(date_object)

#Print today's year, month and day
from datetime import date
today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#use of math module
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)

import math
x = math.pi
print(x)

import math
print(math.log10(10))