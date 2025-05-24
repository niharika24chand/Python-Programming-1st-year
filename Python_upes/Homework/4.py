my_list = [1, 2, 3]
my_list.append(4)
print("After append:", my_list)  

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("After extend:", list1)  

numbers = [10, 20, 30]
numbers.insert(1, 15)  
print("After insert:", numbers)  

fruits = ["apple", "banana", "cherry", "apple"]
fruits.remove("apple")
print("After remove:", fruits)  

nums = [10, 20, 30, 40]
removed = nums.pop()  
print("After pop:", nums)  
print("Popped element:", removed)  

nums.pop(1)  
print("After pop at index 1:", nums)  

colors = ["red", "green", "blue", "green"]
index_green = colors.index("green")
print("Index of 'green':", index_green)  

numbers = [1, 2, 3, 1, 4, 1, 5]
count_ones = numbers.count(1)
print("Count of 1:", count_ones)  

values = [5, 2, 9, 1, 5, 6]
values.sort()
print("After sort:", values)  

values.reverse()
print("After reverse:", values)  

original_list = [10, 20, 30]
copied_list = original_list.copy()
print("Copied list:", copied_list)