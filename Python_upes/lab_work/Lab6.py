#1.	Create a dictionary having name and age, first ask from user how many pairs of name and age user wants to add, then get many number of pairs from user one by one using loop. 
"""
data = {}
n = int(input("How many pairs of name and age do you want to add? "))
for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    data[name] = age
"""

#2.	Now display the pair one by one through loop. 
for name, age in data.items():
    print(f"{name}: {age}")

#3.	Add new pair of name and age through function. 
def add_pair(name, age):
    data[name] = age

#4.	Delete pair of name and age through function.
def delete_pair(name):
    if name in data:
        del data[name]

#5.	Update age corresponding to a name.
def update_age(name, age):
    if name in data:
        data[name] = age

#6.	Display the count of key value pair available in dictionary.
print("Total pairs:", len(data))
#7.	Display the age corresponding to specific name.
specific_name = input("Enter name to get age: ")
print(data.get(specific_name, "Not found"))


#8.Create a clone of dictionary and show the id of both.
clone_data = data.copy()
print("ID of original:", id(data))
print("ID of clone:", id(clone_data))

#9.Convert two lists into dictionary using zip function.
keys = ["Alice", "Bob", "Charlie"]
values = [25, 30, 35]
new_dict = dict(zip(keys, values))
print(new_dict)

#10.Convert a string into dictionary.
string = "name:John,age:28,city:New York"
dict_from_string = dict(item.split(":") for item in string.split(","))
print(dict_from_string)
