#Date:27 Jan 2025 LAB 2A EXTRA.PDF
"""Q1. Given an integer n, perform the following conditional actions:
i) If n is odd, print Weird
ii) If n is even and in the inclusive range of 2 to 5 , print Not Weird
iii) If n is even and in the inclusive range of 6 to 20, print Weird
iv) If n is even and greater than 20, print Not Weird"""

"""n=int(input("Enter a number:\n"))
if(n%2 == 0 and n>=2 and n<=5):
    print("Not Wierd")
elif(n%2 == 0 and n>=6 and n<=20):
    print("Weird")
elif(n%2 == 0 and n>20):
    print("Not Weird")
else:
    print("Weird")"""

"""Q2 WAP to read an integer n from STDIN. For all non-negative integers i<n, print i2 on a separate line."""

"""n=int(input("Enter a number:\n"))
i=0
while i>=0 and i<n:
    print(i*i)
    i+=1"""

"""Q3 WAP to read an integer from STDIN. Without using any string methods, print the following on a single
line: 123…n (Note that … represents the consecutive values in between.)"""

"""n=int(input("Enter a number:\n"))
for i in range(1,n+1):
    print(i,end="")"""

"""Q4 Alternate numbers pattern using a while loop.
Pattern:  1
          3 3
          5 5 5
          7 7 7 7
          9 9 9 9 9
"""

"""i=1 #i=row
n=1 #n=current number
while i<=5:
    j=1 #j=column
    while j<=i:
        print(n,end=" ")
        j+=1
    print()
    i+=1
    n+=2"""

"""Q5 Reverse number pattern: 
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
"""row=5 
for i in range (row,0,-1):
    print(" ".join(str(i)*i))""" #str(i) coverts the number into a string and '*i' repeats the string i times.

"""Q6 Pattern:-
5 4 3 2 1
4 3 2 1
3 2 1 
2 1 
1
"""

"""row=5 
for i in range (row,0,-1):
    print(" ".join(str(j) for j in range(i,0,-1)))"""

"""Q7 Downward half-Pyramid Pattern of Star:
* * * * *
* * * * 
* * *
* *
*
"""

"""row=5 
s='*'
for i in range (row,0,-1):
    print(" ".join(str(s)*i))"""