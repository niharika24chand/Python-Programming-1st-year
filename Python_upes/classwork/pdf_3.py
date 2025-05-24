#Date:27 jan 2025 LAB 3.PDF
"""
Demonstrate the usage of conditional, iterative and control statements through the following
programs. Also understand the concept of strings, and related functions in it:
a) Get a number from user and print number is even/odd and prime/non prime.
"""
"""n=int(input("Enter a number: "))
c=0
for i in range(1,n+1):
    if n%i == 0:
        c+=1

if c==2:
    print("Prime number")
else:
    print("Not a prime number")

if n%2 == 0:
        print("Even  number")
else:
        print("Odd number")
"""

#b)Get the string from the user and print it in forward and reverse order character by character using loop, don't use any built in function.
"""s=input("Enter a string: ")
length=0
for i in s:
    length+=1

print("Forward order: ", end="")
for ch in s:
    print(ch,end=' ')

print()

print("Reverse order: ", end="")
index=length - 1
while index >= 0:
    print(s[index], end=" ")
    index -= 1
"""

#c) WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
"""s=input("Enter a string: ")
sub=input("Enter a substring: ")
c=0
strlen=len(s)
sublen=len(sub)

for i in range(strlen):
    if s[i:(i+sublen)] == sub:  #i+sublen takes that number of characters and i: this takes the character from that position for eg input ABCDCCDC in 2nd iteration s[1;4] this means we will take 4 characters from the beginning ABCD ansd check in this from position 1 means BCD
        c+=1

print("Number of time substring occurs = ",end="")
print(c)
"""

#d) WAP to input the first name, middle and last name of a person. Your task is to print the initials of  the first and middle name separated by a dot (.)  The last name should be followed by a dot and a space where the first letter is capital.
"""fn=input("enter your first name: ")
mn=input("enter your middle name: ")
ln=input("enter your last name: ")
initials=fn[0].upper()+"."+mn[0].upper()+"."

print("User name is:",initials,ln)
"""

#e) Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same. 
s= input("Enter a string: ").upper()  # Convert entire string to uppercase

# Create a list to store frequency of 26 alphabets (A-Z)
frequency = [0] * 26  

# Count occurrences manually
for ch in s:
    if 'A' <= ch <= 'Z':  # Only count alphabets
        index = ord(ch) - ord('A')  # Convert character to index (A=0, B=1, ...)   ord() function in Python returns the Unicode (ASCII) integer value of a character.
        frequency[index] += 1

# Display results
for i in range(26):  # Loop through A-Z
    if frequency[i] > 0:  # Only print letters that appear in input
        print(f"{frequency[i]}{chr(i + ord('A'))}")

    