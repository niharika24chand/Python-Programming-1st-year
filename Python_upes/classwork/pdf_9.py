# Code to demonstrate Implementation of stack using list   
x = ["Python", "C", "Android"]   
x.append("Java")     # To add an item to the top of the stack, use append(). 
x.append("C++")   
print(x)   
print(x.pop())   
print(x)   
print(x.pop())   
print(x)

# Python program to demonstrate queue implementation using list
queue = []   # Initializing a queue
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

