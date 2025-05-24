#add 3 no.
a=int(input("Enter number 1"))
b=int(input("Enter number 2"))
c=int(input("Enter number 3"))
print(a+b+c)

#area of a circle
r=float(input("Enter the radius"))
print("Area of circle is ",2*22*r/7)

#area of rectangle
l=int(input("Enter length"))
b=int(input("Enter breadth"))
print("Area of rect is", l*b)

#avg of 3 no.
a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
c=int(input("Enter number 3 "))
print("Avrage of 3 number is :",(a+b+c)/3)

#avg of 5 sub
a=int(input("Enter marks of subject 1 "))
b=int(input("Enter marks of subject 2 "))
c=int(input("Enter marks of subject 3 "))
d=int(input("Enter marks of subject 4 "))
e=int(input("Enter marks of subject 5 "))
print("Avrage of marks are : ",(a+b+c+d+e)/5)

#cube root of 3
a=int(input("Enter the number"))
print("Cube root of a number is ",a**(1/3))

#Exchange value
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
a,b=b,a
print(a,b)

#odd even
a=int(input("Enter the number"))
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")