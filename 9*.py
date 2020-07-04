'''
Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found.
'''

list_search = [54,587,65,54,78,54,6,8]


def binary_search(list_search, low, high, number):

    if(high>=low):
        mid  = (high + low) //2
        if number == list_search[mid]:
            return mid
        elif number < list_search[mid]:
            binary_search(list_search, low, mid-1, number)
        elif number > list_search[mid]:
            binary_search(list_search, low, mid+1, number)

    else:
        return -1

number = 54
index = binary_search(list_search, 0, len(list_search)-1, number)


if index == -1: 
    print("Not Found")

# is not functioning
    
else:
    print(f"{number} was found at index {index} ")