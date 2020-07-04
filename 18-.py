'''
Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
'''
import json

#help(json)


#serialising

mapping = {"Name":"Pooja", 'Age':21}
with open("mapping.json", "w") as file:
    json.dump(mapping, file)

#deserializing

with open("mapping.json", "r") as file:
    info = json.load(file)
print(info)