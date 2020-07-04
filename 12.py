#Create a function, is_palindrome, to determine if a supplied word is
#the same if the letters are reversed.

def is_palindrome(word):
    length = len(word)
    if length % 2 == 0:
        mid = length / 2
        mid = int(mid)
        first_half = word[:mid]
        second_half = word[mid:]
        second_half = second_half[::-1]
        if first_half == second_half:
            print("First Half: ", first_half)
            print("Second Half:", second_half[::-1])
            print("Palindrome")
            
    else:
        print("Sorry, not a palindrome")

is_palindrome("123321")
        