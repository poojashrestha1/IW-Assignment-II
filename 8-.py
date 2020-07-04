#Write a function, is_prime, that takes an integer and returns True if
#the number is prime and False if the number is not prime.

def is_prime(integer):
    integer = int(integer)
    if integer > 1:
        for i in range(2,integer):
            if (integer % i) == 0:
                return False
            else:
                return True
    else:
        return False

print(is_prime(91))
