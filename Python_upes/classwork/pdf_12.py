"""f1=open("demo.txt")
#f = open("demo.txt", "rt")  #"r" for read, and "t" for text are the default values, you do not need to specify them.
print(f1.read())

f2=open("D:\Python\demo.txt","r")  #If the file is located in a different location
print(f2.read()) 

#Return the 5 first characters of the file:
f1=open("demo.txt")
print(f1.read(5))

#You can return one line by using the readline() method:
f1=open("demo.txt")
print(f1.readline())

#By calling readline() two times, you can read the two first lines:
f1=open("demo.txt")
print(f1.readline())
print(f1.readline())

#Loop through the file line by line:
f=open("demo.txt")
for x in f:
    print(x)
f.close() #it's a good practice to close a file after it's used.

#open file in append mode
f = open("demo.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demo.txt", "r")
print(f.read())

#open the file in write mode the content will get over written.
f = open("demof1.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demof1.txt", "r")
print(f.read())
"""

""" "x" - Create - will create a file, returns an error if the file exist
"a" - Append - will create a file if the specified file does not exist
"w" - Write - will create a file if the specified file does not exist """


"""#Delete a file
import os
os.remove("demof1.txt")
"""

"""
# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
"""

"""
# open the file file2.txt in read mode
fileptr = open("demof2.txt","r")
#initially the filepointer is at 0
print("The filepointer is at byte :",fileptr.tell())
#reading the content of the file
content = fileptr.read()
#after the read operation file pointer modifies. tell() returns the location of the fileptr.
print("After reading, the filepointer is at:",fileptr.tell())
"""

"""
#seek() method which enables us to modify the file pointer position externally.
# open the file file2.txt in read mode
fileptr = open("demof2.txt","r")
#initially the filepointer is at 0
print("The filepointer is at byte :",fileptr.tell())
#changing the file pointer location to 10.
fileptr.seek(10)
#tell() returns the location of the fileptr.
print("After reading, the filepointer is at:",fileptr.tell())
"""



