# #program to input two numbers and print their sum
"""num1=int(input("enter a number :"))
num2=int(input("enter a number :"))
sum=num1+num2
print("sum of two numbers is: ",sum)"""

# #program to input sides of a square and print it's area
"""side=int(input("enter side: "))
area=side*side
print("area of the given square= ",area)"""

#program to input two floating point numbers and print their average
"""num1=float(input("enter first number: "))
num2=float(input("enter second number: "))
avg=(num1+num2)/2.0
print("average of given two numbers =",avg)"""

#program to input two integer numbers a and b. Print true if a is greater than or equal to b else print false
"""a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
if(a >= b):
    print("True")
else:
    print("False")"""

#write a program to check if the number entered by the user is even or odd
""" num=int(input("enter a number:"))
if(num%2 == 0):
    print("number is even")
else:
    print("number is odd") """

#input 3 integers and find the greatest out of them
""" num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
grt=num1
if(num2 > grt):
    grt=num2
elif(num3 > grt):
    grt=num3
else:
    grt=num1

print("greatest number=" , grt) """

#program to check whether the given number is a multiple of seven or not
""" num=int(input("enter a number:"))
if(num%7 == 0):
    print("Number is a multiple of seven")
else:
    print("not a multiple of seven") """

#store following word meaning in python dictionary:
""" table : "a piece of furniture" , "list of facts and figures"
#  cat : "a small animal" """
# info={
#     "table":["a piece of furniture", "list of facts and figure"],
#     "cat":"a small animal"
# }
# print(info)

#you are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
""" stu_list={"python","java","C++","python","javascript","java","python","java","C++","C"}
count=len(stu_list)
print("number of rooms needed= ",count) """

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
""" grade={}
s1=input("enter maths marks: ")
s2=input("enter chemistry marks: ")
s3=input("enter physics marks: ")
grade["math"]=s1
grade["chem"]=s2
grade["phy"]=s3
print(grade) """

#Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)

#METHOD1
""" store={9,"9.0"}
print(store)

#METHOD2(using built-in data type)
store={
    ("int",9),
    ("float",9.0)
}
print(store) """

# Print numbers from 1 to 100
""" count=1
while(count<=100):
    print(count)
    count+=1

print("loop ended") """

#print numbers from 100 to 1
""" count=100
while(count>=1):
    print(count)
    count-=1

print("loop ended") """

#print the multiplication table of a number n(let the number=5).
""" n=int(input("enter a number to generate table: "))
i=1
while(i<=10):
    print(n*i)
    i+=1 """

#print the elements of the following list using a loop {1,4,9,16,25,36,49,64,81,100}

#METHOD1
""" n=1
while n<=10:
    print(n*n)
    n+=1 """

#METHOD2
""" store=[1,4,9,16,25,36,49,64,81,100]
idx=0
n=len(store)
while(idx < n):
    print(store[idx])
    idx+=1 """

#find a number x in the tuple {1,4,9,16,25,36,49,64,81,100}.
""" nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter number to be searched:"))
i=0
while i < len(nums):
    if(nums[i] == x):
        print("found at index",i)
        break
    else:
        print("finding..")
    i+=1 """

#print the elements of the following list using for loop: [1,4,9,16,25,36,49,64,81,100]
""" nums=[1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)
else:
    print("all elements have been printed") """

#Search for a number x in this tuple using for loop: [1,4,9,16,25,36,49,64,81,100] also print the index.
#(this type of search is know as linear search.)
""" tup=(1,4,9,16,25,36,49,64,81,100)  
x=int(input("enter the number to be searched: "))
idx=0
for val in tup:
    if(val == x):
        print("number found at index",idx)
        break
    idx+=1

else:
    print("number not found") """

#do the following questions using for and range():

#ques1 print numbers from 1 to 100
""" nums=range(1,101)
for val in nums:
    print(val) """

#ques2 print numbers from 100 to 1
""" nums=range(100,0,-1)
for val in nums:
    print(val) """

#ques3 print the multiplication table of a number n
""" n=int(input("enter a number: "))
tab=range(1,11)
for i in tab:
    print(n*i) """

#WAP to find the sum of first n numbers using while loop
""" n=int(input("enter the limit: "))
i=0
sum=0
while (i<=n):
    sum+=i
    i+=1

print("sum=",sum) """

#WAP to find factorial of first n numbers using for loop
""" n=int(input("enter limit:"))
num=range(1,n+1)
fact=1
for i in num:
    fact=fact*i

print("factorial =",fact) """

#print the length of a list.(list is the parameter)
""" def length(list):
    return len(list)
 
games=["badminton","tennis","chess"] 
output=length(games)
print("length of list=",output) """

#WAF to print the elements of a list in a single line.(list is the parameter)
""" def print_names(list):
    for val in list:
        print(val,end=" ")

names=["jatin","ayushi","shraddha","anil"]
print_names(names) """

#WAF to find the factorial of a number n. (n is the parameter)
""" def cal_fact(n):
    i=1
    fact=1
    while(i <= n):
        fact=fact*i
        i+=1
    return fact

x=int(input("enter a number:"))
output=cal_fact(x)
print("factorial =" ,output ) """

#WAF to convert USD to INR.
""" def convert(USD):
    INR=USD*85.77
    return INR

money=int(input("enter your amount:"))
print("amount in INR",convert(money)) """

#WAF to check if the given number is odd or even (the number is the parameter)
""" def check(num):
    if(num%2 != 0):
        print("ODD")
    else:
        print("EVEN")

n=int(input("enter a number:"))
check(n) """

# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/0
# using Java
# I like programming in Java.
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java\nI like programming in Java")

#WAF that replace all occurrences of "java" with "python" in above file.
""" with open("practice.txt","r") as f:
    data=f.read()

def rep(d):
    new_data=d.replace("Java","Python")
    return new_data

output=rep(data)
print(output) """

#Search if the word "learning" exists in the file or not
""" with open("practice.txt","r") as f:
    data=f.read()

def search(d):
    result=d.find("learning")
    return result

output=search(data)
if(output == -1):
    print("word does not exist")
else:
    print("word exista at index=",output) """

#WAF to find in which line of the file does the word "learning"occur first.Print -1 if word not found
""" def check_line():
    word = "learning"
    data = True
    count = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print("word found on line number:",count)
                return
            count+=1
        return -1

print(check_line()) """

#From a file containing numbers separated by comma, print the count of even numbers.
""" with open("num.txt","r") as f:
    data=f.read()

count=0
nums=data.split(",")
for val in nums:
    if(int(val) %2 == 0):
        count+=1

print("total even numbers =",count) """

#Create student class that takes name & marks of 3 subjects as arguments in constructor Then create a method to print the average
""" class Grades:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def cal_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your average marks is",sum/3.0)

s1=Grades("yash",[95,92,91])
s1.cal_avg() """

#Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
""" class Account():
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amt):
        self.balance-=amt
        print("Rs.",amt,"has been debited from your account number:",self.account_no)
        print("Rs",self.print_bal(),"is your current balance")

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"has been credited to your account number:",self.account_no)
        print("Rs",self.print_bal(),"is your current balance")

    def print_bal(self):
        return self.balance

acc1=Account(10000,54126)
acc1.debit(3000)
acc1.credit(1000)
acc1.print_bal() """

#program to print the sum of two complex numbers (using dunder function) #this is an example of polymorphism(operator overloading)
""" class Complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2): #(__add__ is a dunder function)
        newReal=self.real + num2.real
        newImg=self.img + num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,8)
num2.showNumber()

result=num1+num2 #(this would have show error if dunder function was not used)
result.showNumber() """

# Define a Circle class to create a circle with radius r using the constructor. Define an Area method of the class which calculates the area of the circle.Define a Perimeter method of the class which allows you to calculate the perimeter of the circle.
""" class Circle():
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*(self.radius**2)

    def perimeter(self):
        return 2*(22/7)*(self.radius**2)



cir1=Circle(21)
print("area of the circle = ",cir1.area())
print("perimeter of the circle = ",cir1.perimeter()) """

# Define a Employee class with attributes role, department & salary. This class also has a showDetails() method. Create an Engineer class that inherits properties from Employee & has additional attributes : name &age.
""" class Employee():
    def __init__(self,role,dep,sal):
        self.role=role
        self.dep=dep
        self.sal=sal

    def showDetails(self):
        print("Employee details are:\n","Role :",self.role,"\nDepartment :",self.dep,"\nSalary :",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("HOD","Cyber","30lakh")

    def per_details(self):
        print("Employee name :",self.name,"\n Employee age :",self.age)

emp1=Engineer("Niharika Chand",22)
emp1.per_details()
emp1.showDetails() """

#Create a class Order which stores item and it's price. Use dunder function __gt__()to convey that: order1>oder2 if price of order1>price of oder2.
"""class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def showDetails(self):
        print("item:",self.item,"\nprice:Rs",self.price)

    def __gt__(self,od2):
       return self.price > od2.price

od1=Order("perfume",560)
od1.showDetails()

od2=Order("face mask",330)
od2.showDetails()

result=od1>od2
if(result == True):
    print("Order 1 is greater than order 2")
else:
    print("Order 2 is greater than order 1")"""






