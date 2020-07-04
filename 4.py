'''
Create a list. Append the names of your colleagues and friends to it.
Has the id of the list changed? Sort the list. What is the first item on
the list? What is the second item on the list?
'''

names = []
print(id(names))

names.append("Pooja")
names.append("Ram")
names.append("Shyam")
names.append("Sita")
names.append("Geeta")

print(id(names))

#Yes, they are.

print("Before sorting: ", names)
names.sort()
print("After sorting: ", names)
print("First item: ", names[0])
print("Second item:", names[1])
