'''
Create a list of tuples of first name, last name, and age for your
friends and colleagues. If you don't know the age, put in None.
Calculate the average age, skipping over any None values. Print out
each name, followed by old or young if they are above or below the
average age.
'''
friends = [("Ram", "Shakya", 30), ("Hari", "Bahadur", 20), ('Sita', 'Maya', 10), ("Riya", "Tamang", None)]

sum = 0
total_entry = len(friends)
total_entry = int(total_entry)

for i in friends:

    if i[2] is not None:
        sum = sum + i[2]

    average = sum/total_entry   


print("Average age is: ", average)

for i in friends:
    if i[2] is None:
        print(f"{i[0]}'s age is not known .")
    elif i[2] is not None and float(i[2]) < average:
        print(f"{i[0]} is young and is {i[2]} years of age.")
    elif i[2] is not None:
        print(f"{i[0]} is older and is {i[2]} years of age.")
        


