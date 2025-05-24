 #Date:5 feb 2025 LAB 4a.PDF
#List
"""
Height = [1.73 , 1.68, 1.76 ] #Storing heights of persons in Height
print(Height)

#you want to store height and name both then
Height = [“rahul”, 1.75, “person”, 1.63, “person2”, 1.96]
print(Height)

#Nested list is possible
Person_heights = [[“person1”, 1.75] , [“person2”, 1.68]]
print(Person_height)

#Example1:
Values = [ 1, 2, 3, 4,5, 6]
Values[0] = 9
print(Values)

#List allows duplicate:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Use of length function in list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Example2:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list4)
print(type(list1))
print(list1[1])

#Negative indexing:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Example3:
b= [5,10,15,20,25] 
#printing upto 3 indices
print(b[:3]) #b[0:3}

#reversing a list with use of slicing
print(b[::-1])

#printing from indices 1 to 3
print(b[1:3])

#By leaving out the start value, the range will start at the first item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])

#To check if item exist:
l=["apple","banana","cherry"]
if("apple" in l):
print("Yes,'apple' is in the fruits list")

#To change the value of a specific item:
thislist=["apple","banana","cherry"]
thislist[1]="blackcurrant"
print(thislist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Some python expressions for list:
len([1,2,3]) #to calculate length 

[1,2,3]+[4,5,6] #concatenation

['Hi!'*4] #for repetition

3 in [1,2,3] #for membership

for x in [1, 2, 3]: 
    print(x)    #for iteration

#Deleting an item from the list:
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

#Python list method remove() searches for the given element in the list and removes the first matching element.
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print ("List : ", aList)
aList.remove('abc')
print ("List : ", aList)
"""



