#1. add three numbers
"""a=int(input("enter a number:\n"))
b=int(input("enter a number:\n"))
c=int(input("enter a number:\n"))
print("sum =",a+b+c)"""

#2. Add two strings (string concatenation)
"""str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Concatenated String:", str1 + str2)"""

#3. Find area of rectangle.
"""length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area_rectangle = length * breadth
print("Area of Rectangle:", area_rectangle)"""

#4. Find area of circle. 
"""radius = float(input("Enter radius: "))
area_circle = 3.1416 * radius * radius
print("Area of Circle:", area_circle)"""

#5. Find cubic root of a number.
"""num = float(input("Enter a number: "))
cubic_root = num ** (1/3)
print("Cubic Root:", cubic_root)"""

#6. Average of three numbers.
"""avg = sum_numbers / 3
print("Average of three numbers:", avg)"""

#7.	Exchange the Values of Two Numbers Without Using a Temporary Variable
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping: a =", a, ", b =", b)"""

#8. Perform operations on String
"""string = input("Enter a string: ")
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Length:", len(string))
print("Reverse:", string[::-1])"""

#9.	Determine whether the given number is even or odd. 
"""num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")"""

#10. Marks of a student in five subjective are acquired. Determine average marks and grade.
"""O   91-100 
A+ 81 -90
A  71 - 80
B+ 61-70
B 51 - 60
C+ 41 - 50
C 35 - 40
Fails otherwise
"""
marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))

total_marks = sum(marks)
avg_marks = total_marks / 5

if avg_marks >= 91:
    grade = "O"
elif avg_marks >= 81:
    grade = "A+"
elif avg_marks >= 71:
    grade = "A"
elif avg_marks >= 61:
    grade = "B+"
elif avg_marks >= 51:
    grade = "B"
elif avg_marks >= 41:
    grade = "C+"
elif avg_marks >= 35:
    grade = "C"
else:
    grade = "Fails"

print("Average Marks:", avg_marks)
print("Grade:", grade)