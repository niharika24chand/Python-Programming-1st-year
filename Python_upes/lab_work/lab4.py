#Create the list through different ways, and display the list content (directly, through loop, slicing etc.)
l=["apple",28,"banana","mango",30,28]
print(l) #directly

for i in l: #loop
    print(i)

print(l[0]) #index
print(l[3])
print(l[1:4]) #slicing
print(l[::-1]) #reverse

#list cloning
c=l[:]
print("Original list: ",l)
print("Cloned list: ",c)

#append, insert, extend, count, remove, pop, sort, max, min function
l.append("grapes") #append
l.insert(3,"watermelon") #insert
l.extend("kiwi") #extend
print(l.count("i")) #count
print(l)
l.remove("i") #remove
l.pop(5) #pop
print(l)

f=[28,91,11,3,43,22,54,96]
f.sort() #sort
print(f)

m=max(f)
n=min(f)
print("Maximum = ",m) #max
print("Minimum = ",n) #min