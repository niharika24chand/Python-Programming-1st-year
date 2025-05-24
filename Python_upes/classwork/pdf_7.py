"""import mymodule
mymodule.greeting("Jonathan")

import mymodule
a = mymodule.person1["age"]
print(a)

import file
name = input("Enter the name?") 
file.displayMsg(name)

from calculation import summation    #it will import only the summation() from calculation.py 
a = int(input("Enter the first number")) 
b = int(input("Enter the second number")) 
print("Sum = ",summation(a,b))    #we do not need to specify the module name while accessing summation()

from math import*  #if we don't use '*' then we will have to write math.sqrt 
print(sqrt(16))

#Renaming a module
import calculation as cal; 
a = int(input("Enter a?")); 
b = int(input("Enter b?")); 
print("Sum = ",cal.summation(a,b))

#The dir() function returns a sorted list of names defined in the passed module. 
import datetime
List = dir(datetime) 
print(List) 
"""

#creating a package and employee example is in the folder named main. 
