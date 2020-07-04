#Create a list with the names of friends and colleagues. Search for the
#name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

friends = ['Ram', 'Shyam', 'Hari', 'Rita', 'Sita']

for friend in friends:
    if friend == 'John':
        print("Found")
        break
else:
    print("Not Found")


