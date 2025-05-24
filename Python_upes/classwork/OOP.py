#object creation
"""class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)
c1 = car("Toyota", 2016)
c1.display()"""

#creating classes
"""class Employee:
    id = "C123"
    name = 'TCS'
    def display (self):
        print(self.id, self.name)
#creating object
emp1=Employee()
emp1.display()"""

#class and instance variable
"""class Student:
    name='TCS' # Class variable
    id='C123'  # Class variable
    def display_details(self):
        print("Name: ",self.name, "ID: ",self.id ,"age: ",self.age)
s = Student()
s.name = 'amit' # Instance variable
s.id = 112      # Instance
s.age = 23      # Instance
s.display_details()
print(Student.name)
print(Student.id)"""

#constructor
"""class Employee:
    def __init__(self, name, id): #paramterized constructor in python
        self.id = id
        self.name = name
    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))
emp1 = Employee("Gagan", 101)
emp2 = Employee("Kavita", 102)
emp1.display()
emp2.display()"""

#Constructor- non parameterized
"""class Student:
    def __init__(self):
        print("This is non parametrized constructor")
    def show(self,name):
        print("Hello",name)
student = Student()
student.show("Susheel")"""

#When we do not include the constructor in the class or forget to declare it, then that becomes the default constructor.
"""class Student:
    roll_num = 999999 # say a default roll no
    name = "Anonymous" # anonymous name
    def display(self):
        print(self.roll_num,self.name)
st = Student()
st.display()"""

#when multiple constructors are used only the last one is considered.
"""class Student:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The second contructor")
st = Student()"""

#example
"""class Student:  
    def __init__(self):  
        print("The first contructor")  
        self.name='LK'
        self.id=184 
    def __init__(self,name,id):
        print("The second contructor")  
        self.name=name
        self.id=id 
    def display(self):
        print("Name: ",self.name)
        print("ID: ",self.id)
 #st1 = Student()  This line will cause error
 #st1.display() This line will cause error
st2 = Student('ajay',1234)
st2.display()"""

#To count the no of instances created for a class use class/static variables
class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1
s1=Student()
s2=Student()
s3=Student()
print("The number of students: ",Student.count)
# Since count is static variable its value is common for all instances of Student.

#q10
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

# creates the object of the class Student
s = Student("Amit", 101, 22)

# prints the attribute name of the object s
print(getattr(s, 'name'))  # Output: Amit

# reset the value of attribute age to 23
setattr(s, "age", 23)

# prints the modified value of age
print(getattr(s, 'age'))  # Output: 23

# prints True if the student contains the attribute with name id
print(hasattr(s, 'id'))  # Output: True

# deletes the attribute age
delattr(s, 'age')

# check if 'age' exists before accessing it
if hasattr(s, 'age'):
    print(s.age)
else:
    print("Attribute 'age' has been deleted.")  # Safe handling of deleted attribute

#q11
class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age 
        def display_details(self):
            print("Name:%s, ID:%d, age:%d"%(self.name,self.id))
s = Student("Amit",101,22)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)

#q12
class Example:
    def __init__(self):
        print ("Object created");
        # destructor
        def __del__(self):
            print ("Object destroyed");
# creating an object
myObj = Example()
# to delete the object explicitly
del myObj

#q14
class Animal:
    def run(self):
        print("Animal running")

# The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("Dog barking")

# The child class Puppy inherits from Dog
class Puppy(Dog):
    def eat(self):
        print("Eating bread...")

# Creating an instance of Puppy
p = Puppy()
p.bark()  # Inherited from Dog
p.run()   # Inherited from Animal
p.eat()   # Defined in Puppy

#q15
class Calculation1:
    def summation(self, a, b):
        return a + b

class Calculation2:
    def multiplication(self, a, b):
        return a * b

class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a / b

# Creating an instance of Derived
d = Derived()

# Calling methods from parent classes
print(d.summation(10, 20))      # Output: 30
print(d.multiplication(10, 20)) # Output: 200
print(d.divide(10, 20))         # Output: 0.5

#q16
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver code
object1 = Child1()
object2 = Child2()

object1.func1()  # Inherited from Parent
object1.func2()  # Defined in Child1

object2.func1()  # Inherited from Parent
object2.func3()  # Defined in Child2

#q17
class Calculation1:
    def summation(self,a,b):
        return a+b
class Calculation2:
    def multiplication(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d = Derived()
print(issubclass(Derived,Calculation2))
print(isinstance(d,Calculation1))


