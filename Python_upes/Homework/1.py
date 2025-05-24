name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

s = "12345"
if s.isdigit():
    print("The string contains only numbers.")
else:
    print("The string contains non-numeric characters.")


s = "apple,banana,cherry"
split_list = s.split(",")
print(split_list)

words = ["apple", "banana", "cherry"]
result = "-".join(words)
print(result)

s = "Hello, World!"
uppercase = s.upper()
print(uppercase)  

lowercase = s.lower()
print(lowercase)