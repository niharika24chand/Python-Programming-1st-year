#Exception handling

try:
    print(x)    #since we don't have the value of x so there's an error hence the except block will run
except:
    print("An exception occurred")

#Print one message if the try block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#You can use the else keyword to define a block of code to be executed if no errors were raised
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# The finally block, if specified, will be executed regardless if the try block raises an error or not
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

#Python program to handle exception
try:
    f = open("demofile.txt",'w')
except:
    print("hhSomething went wrong when writing to the file")
finally:
    f.close()
    print("h")


