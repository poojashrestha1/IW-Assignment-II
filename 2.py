#Write an if statement to determine whether a variable holding a year
#is a leap year.

year = int(input("Enter the Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")



#reference from beginner's book

