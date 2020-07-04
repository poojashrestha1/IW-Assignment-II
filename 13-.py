#Write a function to write a comma-separated value (CSV) file. It
#should accept a filename and a list of tuples as parameters. The
#tuples should have a name, address, and age. The file should create
#a header row followed by a row for each tuple.

import csv

csv_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

with open('csvfile.csv', 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerow(["Name", "Address", "Age"])
    for data in csv_list:
        writer.writerow(data)

with open('csvfile.csv', 'r') as file:
    reader = csv.reader(file, delimiter=' ', escapechar=' ', quoting = csv.QUOTE_NONE)
    for data in reader:
        print(data)
    
