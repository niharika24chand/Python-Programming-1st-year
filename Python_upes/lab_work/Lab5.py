#Generate squares of all the integers from 1 to 50.
"""
n=1
print("Squares till 50 are: ")
while n<=50:
    sq=n*n
    print(sq)
    n=n+1
"""

#Count the number of characters in a string using a loop.
"""
str=input("Enter a string: ")
c=0
for ch in str:
    c+=1
print("Total number of characters = ",c)
"""

#Print a string in reverse. 
"""
str=input("Enter a string: ")
rev = ""
for ch in str:
    rev= ch + rev
print(rev)
"""

#Find all the prime numbers below 50.
"""
def prime(num):
    c=0
    for i in range(1, num + 1):
        if num % i == 0:
            c+=1
    if(c==2):
        print(num)

n=1
while n<=50:
    prime(n)
    n+=1
"""

#Print Armstrong numbers in the range 1 to 1000. An Armstrong number is a number whose sum of the cubes of the digits is equal to the number itself. For example, 370 = 33+73+03
"""
def armstrong(num):
    sum=0
    temp=num
    while temp> 0:
        d = temp % 10
        sum += d ** 3
        temp //= 10

        if(sum == num):
            print(num)

print("Armstrong numbers in the range of 1 to 1000 are: ")
n=1
while n<=1000:
    armstrong(n)
    n+=1
"""






