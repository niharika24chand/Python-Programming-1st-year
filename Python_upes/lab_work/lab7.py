#LAB 7: To demonstrate the different built in functions

#Ques1. Get some numeric element in a list and find the sum of elements of list using map and lambda function
"""numbers = [100, 150, 200, 250, 300]
result = sum(map(lambda x: x, numbers)) ## Use lambda with map to keep elements unchanged, then sum the mapped result

print("Sum of the elements in the list:", result)"""

#Ques2.	Get the age of students in a list and display those students who are above 18, use lambda and filter function.
"""ages = [19, 13, 15, 20, 25, 9, 22, 16]
above_18 = list(filter(lambda age: age > 18, ages)) ## Using lambda with filter to get students whose age is greater than 18

prin("Students with age above 18:", above_18)"""

#Ques3.	Get the name and age of students from user in a dictionary and return two different dictionary where entry of dictionary are sorted by name and age respectively. Use customized sorted() function.
"""def get_sorted_dictionaries(students):
    # Sort dictionary by name (alphabetically)
    sorted_by_name = dict(sorted(students.items(), key=lambda item: item[0]))

    # Sort dictionary by age (numerically)
    sorted_by_age = dict(sorted(students.items(), key=lambda item: item[1]))

    return sorted_by_name, sorted_by_age

# Get user input and store it in a dictionary
num_students = int(input("Enter the number of students: "))
students = {}

for _ in range(num_students):
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    students[name] = age

# Get the sorted dictionaries
sorted_name_dict, sorted_age_dict = get_sorted_dictionaries(students)

# Print the sorted dictionaries in a more readable format
print("\nDictionary sorted by name (ascending):")
for key, value in sorted_name_dict.items():
    print(f"{key}: {value}")

print("\nDictionary sorted by age (ascending):")
for key, value in sorted_age_dict.items():
    print(f"{key}: {value}")
"""

#Ques4.	Demonstrate the concept of closure function
"""def outer_function(message):
    def inner_function():
        print(f"Message is: {message}")  # Accessing `message` from the outer scope
    return inner_function  # Returning the inner function

# Create a closure
closure_instance = outer_function("Hello, this is a closure!")

# Call the closure
closure_instance()  # Output: Message is: Hello, this is a closure!
"""