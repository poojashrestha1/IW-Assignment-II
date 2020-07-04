#Create a tuple with your first name, last name, and age. Create a list,
#people, and append your tuple to it. Make more tuples with the
#corresponding information from your friends and append them to the
#list. Sort the list. When you learn about sort method, you can use the
#key parameter to sort by any field in the tuple, first name, last name,
#or age.

my_info = ("Pooja", "Shrestha", 20)

people = []
people.append(my_info)

first = ("Ram", "Shakya", 31) 
people.append(first)
second = ("Hari", "Bahadur", 21)
people.append(second)
third = ('Sita', 'Maya', 10)
people.append(third)

print("List before: ", people)

people.sort(key = lambda x: x[2])

print("List after: ", people)

