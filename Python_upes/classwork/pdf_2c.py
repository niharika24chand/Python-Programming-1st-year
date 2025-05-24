#Date(9/01/25)
#program to print a number pyramid.
"""
row=int(input("enter the row: "))
for i in range(1,row+1):
    for j in range(i):
        print(i,end=' ')
    print()
"""

#Date(13/01/25)

#while and break statement example1(ques-exit the loop when i is 3)
"""
i=1
while(i<6):
    if(i==3):
        print(i)
        break
    print(i)
    i+=1
print("hh")
"""

#example2 (while and break)
"""
var = 10 
while var > 0:
    print ('Current variable value :', var)
    var = var -1
    if var == 5:
        break
print ("Good bye!")
"""

#continue statement (example1)
"""
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")
"""

#continue statement(example2) (ques. continue if i is 3)
"""
i=1
while(i<6):
    i+=1
    if(i==3):
        continue
    print(i)
"""

#infinite while loop
"""
while(1):
    print("infinite while loop")"""

#for loop
"""str="Pyhton"
for ch in str:
    print(ch)
"""

#range() function
"""
num=int(input("enter a number:"))
for i in range(1,6,2): #range(start,stop,step size)
    print(i)
"""

#Example (for loop)
#ques. Program to print even number using step size in range().
"""
n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)
"""

#len() function
"""
list = ['Peter','Joseph','Ricky','Devansh']
for i in range(len(list)):
    print("Hello",list[i])
"""

#Program to print number pyramid.
"""
rows=int(input("enter the rows:"))
for i in range(rows+1):
    for j in range(i):
        print(i,end='')
    print()
"""

#nested for loop 
"""
rows = int(input("Enter the rows:"))
for i in range(0,rows+1):
    for j in range(i):
        print("*",end = ' ')
print()
"""

#example1
""" 
for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter :', letter)
"""

#example2
""""
var = 10
while var > 0:
    print 'Current variable value :', var
    var = var -1
    if var == 5:
        break
print "Good bye!" 
"""