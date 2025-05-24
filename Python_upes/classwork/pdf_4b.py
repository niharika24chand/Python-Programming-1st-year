#Date:5 Feb 2025 4b pdf.
#Tuples
"""
#Syntax for declaration of a tuple:
Score = (20,30,55,68,12,32)

#All the different types in Python - String, Integer, Float can all be contained in tuple.
Tuple1 = (‘person’, 20, 12.5)

#Each element of tuple can be accessed via index similar to lists.
tup=('rakesh',23,6.2,False)
print(tup[0])
print(tup[-1])

#  Tuple has immutable nature, i.e., tuple cant be changed or modified after its creation. (REMEMBER THIS)

#Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#To count the number of items in a tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#To create tuple containing only one item:
thistuple = ("apple",)
print(type(thistuple))

#Some python expressions for tuple:
T1=(1,2,3,4,5)
print(len(T1)) #to calculate length 

print(T1+T2) #concatenation

print(T1*2) #for repetition

print (2 in T1)  #for membership

for i in T1:
    print(i)  #for iteration

#count() method returns the number of times a specified value appears in the tuple
thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.count(5)
print(x)

#The index() method finds the first occurrence of the specified value. The index() method raises an exception if the value is not found.
thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.index(7)
print(x)
"""


""" ________________________________________________________________________________________________________"""

"""
#Set

#Creating and printing a set
Set1 = { 1, 2, 1, 3, 4, 5 }
print(Set1)

#Set can also be created from a list
my_set = set([1, 2, 3, 2])
print(my_set)

#To calculate the length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# to print type
myset = {"apple", "banana", "cherry"}
print(type(myset))

#Set Constructor
thisset = set(("apple", "banana", "cherry")) # note the double roundbrackets
print(thisset)

#To create an empty set
a= set()
type(a)

#To access a particular item from a set:
print("banana" in thisset)

#To add items in a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update() : To add items from another set into the current set.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#To remove a particular item from the set (using remove() method).
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#//Note: If the item to remove does not exist, remove() will raise an error. (REMEMBER)

#To remove a particular item from the set (using discard() method).
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#//Note: If the item to remove does not exist, discard() will NOT raise an error.

#del : keyword used to delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#union() : this method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#update() : this method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#ntersection_update() : this method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
"""


""" ________________________________________________________________________________________________________"""

"""
#Dictionary

dict1 = {} #Empty Dictionary declaration

#Example1:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#//Dictionaries cannot have two items with the same key:Duplicate values will overwrite existing values

#To access elements of a dictionary (using get())
d = {1:"hhh","2":"Two"}
print("d[1]=",d[1]) #Accessing with key
print("d[2]=",d.get("2")) #Accessing using get() function

#Manipulating value in a dictionary
my_info = {'name':'Rahul', 'age': 25}
# update value
my_info['age'] = 26
print(my_info) 

#To add items in a dictionary
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict["color"] = "red"
print(thisdict)

#The pop() method removes the item with the specified key name
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item.
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.popitem()
print(thisdict)

#del : keyword used to delete the dictionary completely:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
del thisdict
print(thisdict)

#clear() method empties the dictionary:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.clear()
print(thisdict) 

#using loop in a dictionary
#Print all key names in the dictionary, one by one
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict:
print(x)

#Print all values in the dictionary, one by one
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
for x in thisdict:
print(thisdict[x])

#Loop through both keys and values, by using the items() method:
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
for x, y in thisdict.items():
print(x, y)

#To copy a Dictionary:
t = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
m = t.copy()
print(m)
"""

""" ________________________________________________________________________________________________________"""


#Date:10 feb 2025 LAB 4b PDF (List comprehension)

"""Example 1: Suppose we want to create an output list which contains only the
 even numbers which are present in the input list. Lets see how to do this
 using for loops and list comprehension and decide which method suits better."""
"""
input_list=[1,2,3,4,4,5,6,7,7]
output_list=[]
# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)
print("Output List using for loop:", output_list)

# Using List comprehensions for constructing output list
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
comp_output = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", comp_output)
"""

#Set comprehension
"""Example 1 : Suppose we want to create an output set which contains only the even
 numbers that are present in the input list. Note that set will discard all the duplicate
 values. Lets see how we can do this using for loops and set comprehension."""
"""
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set = set()
# Using loop for constructing output set
for var in input_list:
    if var % 2== 0:
        output_set.add(var)
print("Output Set using for loop:", output_set)

# Using Set comprehensions for constructing output set
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
comp_set = {var for var in input_list if var % 2 == 0}
print("Output Set using set comprehensions:", comp_set)
"""

#Dictionary comprehension
"""Example 1: Suppose we want to create an output dictionary which contains only the
 odd numbers that are present in the input list as keys and their cubes as values. Lets
 see how to dothis using for loops and dictionary comprehension."""
"""
input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {}
# Using loop for constructing output dictionary
for var in input_list:
    if var % 2!= 0:
        output_dict[var] = var**3
print("Output Dictionary using for loop:", output_dict )

# Using Dictionary comprehensions for constructing output dictionary
input_list = [1,2,3,4,5,6,7]
comp_dict = {var:var ** 3 for var in input_list if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:", comp_dict)
"""