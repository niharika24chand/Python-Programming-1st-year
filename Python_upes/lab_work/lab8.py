# To demonstrate the concept of exception handling

# 1. Write a Python program to use try-except-else block
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print(f"You entered: {number}")

# 2. Write a Python program to use try-except-finally block
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Oops! That was not a valid number.")
finally:
    print("This block always runs, no matter what.")

# 3. Write a Python program to write your own exception and throw it.
class NegativeNumberError(Exception):
    def _str_(self):
        return "Negative number not allowed."

def check_number(num):
    if num < 0:
        return False
    else:
        print("Number is valid.")
        return True

try:
    num = int(input("Enter a positive number: "))
    if not check_number(num):
        print(NegativeNumberError())
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# 4. Write a Python program to demonstrate the use of built in modules random and math.
import random
import math

num = random.randint(1, 100)
print(f"Random number: {num}")
print(f"Square root of {num} is {math.sqrt(num):.2f}")

# 5. Write a program to create a module and to use its functionality
import sample_mod

x = 10
y = 5

print("Add:", sample_mod.add(x, y))
print("Subtract:", sample_mod.subtract(x, y))
print("Square of x:", sample_mod.square(x))

