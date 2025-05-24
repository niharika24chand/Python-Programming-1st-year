#Date: 12Feb,2025 LAB 6 Pdf( Different types of Functions in Python)

# Lambda function example:
"""
#using normal function
def doubler(x):
 return x*2
print(doubler(2))

#using lambda function:
doubler = lambda x: x*2
print(doubler(2))
"""

#Some characterstics of lambda function:
"""
#Positional arguments:
add = lambda x, y, z: x+y+z
print(add(2, 3, 4)) #prints 9

# Keyword arguments:
add = lambda x, y, z: x+y+z
print(add(x=2, z=3, y=4)) #prints 9

#Default argument:
add = lambda x, y=3, z=4: x+y+z
print(add(2)) #prints 9

#Variable list of arguments (*args)
add = lambda *args: sum(args)
print(add(2,3,5,7))  #prints 17

#Variable list of keyword arguments (**args)
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3,z=3,f=8))  #prints 16
"""

"""
#If-else using lambda function:
findMin = lambda x, y: x if x < y else y
print(findMin(2, 4))  # Prints 2
print(findMin('a', 'x'))   # Prints a
"""

#Map function:
"""
def doubler(x):
    return x*2
L =[1, 2, 3, 4, 5, 6]
mod_list = map(doubler, L)
print(list(mod_list))   # Prints [2, 4, 6, 8, 10, 12]

# Double each item of the list
L =[1, 2, 3, 4, 5, 6]
doubler = map(lambda x: x*2, L)
print(list(doubler))   # Prints [2, 4, 6, 8, 10, 12]
"""

# Mapping Function in a Dictionary:
"""
dOfNames={7: 'sam', 8: 'john', 9: 'mathew', 10: 'riti', 11 : 'aadi', 12 : 'sachin'}
dOfNames = dict(map(lambda x: (x[0], x[1] + '_'), dOfNames.items()))
print('Modified Dictionary : ')
print(dOfNames)
"""

#Sorted function:
"""
# List
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

 # set
 py_set = {'e', 'a', 'u', 'o', 'i'}
 print(sorted(py_set, reverse=True))

 # dictionary
 py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
 print(sorted(py_dict, reverse=True))

#Sorting according to length:
item=["S","SS","aaaa","cc"]
print(sorted(item, key=len))

# Sort a list of integers based on 
# their remainder on dividing from 7 
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
print ("Normal sort :", sorted(L)) 
print ("Sorted with key:", sorted(L, key = func))

#Sorting Dictionaries:
dt={6:"Sahil",4:"Tarun",5:"Anurag",2:"Ankur",1:"Ravi",3:"Pankaj"}
#sorting dictionary by key values
c1=dict(sorted(dt.items(),key=lambda t:t[0]))
print(c1)
#sorting dictionary by values
c2=dict(sorted(dt.items(),key=lambda t:t[1]))
print(c2)
"""

#Three basic ways to get data from a dictionary:
"""
Dictionary.keys() : Returns only the keys in an arbitrary order.
Dictionary.values() : Returns a list of values.
Dictionary.items() : Returns all of the data as a list of key-value pairs.
"""

"""
#prints sorted keys
dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.keys()
# Sorted by key
print("Sorted by key: ", sorted(lst))

#prints sorted values
dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.values()
#Sorted by value
print("Sorted by value: ", sorted(lst))

#prints sorted items
dict = {}
dict['1'] = 'apple'
dict['3'] = 'orange'
dict['2'] = 'mango'
lst = dict.items()
#Sorted by item
print("Sorted by value: ", sorted(lst))
"""

"""
#Filter function:
def checkAge(age):
    if age > 18:
        return True
    else:
        return False
age = [5, 11, 16, 19, 24, 42]
adults = filter(checkAge, age)
print(list(adults))   # Prints [19, 24, 42]

#Filter function usiong lambda function:
age = [5, 11, 16, 19, 24, 42]
adults = filter(lambda x: x > 18, age)
pr"int(list(adults))   # Prints [19, 24, 42]
"""

"""
# Global Variables:
#Example 1: Create a Global Variable
x = "global"
def foo():
    print("x inside:", x)  # x inside: global
foo()
print("x outside:", x)  #x outside: global

#Local variable:
#Example 2: Accessing local variable outside the scope
def foo():
    y = "localmksfklds"
foo()
print(y) # The output shows an error because we are trying to access a local variable y in a global scope whereas the local variable only works inside foo() or local scope.

#Example 3: Create a Local Variable
def foo():
    y = "local"
    print(y)
foo()

#Example 5: Global variable and Local variable with same name
x = 5 #global
def foo():
    x = 10 #local
    print("local x:", x)
foo()
print("global x:", x)
"""

#Python inner function:
"""
def print_msg(msg):
# This is the outer enclosing function
    def printer():
        # This is the nested function
        print(msg)
    printer()
print_msg("Hello")



#Closure function:
def outer(name):
    def inner():
        print(name)
    return inner
myFunction = outer('Tech')
myFunction()
"""
