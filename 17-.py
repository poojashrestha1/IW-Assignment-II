'''Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors.'''

def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Do not enter 0 as a demominator.")


try:
    operand1 = float(input("Enter a number: "))
    operand2 = float(input("Enter another number: "))


    operator = input("Enter an operator (+,-,*,/): ")

    if operator == '+':
        print("The result is: ", addition(operand1, operand2))
    elif operator == '-':
        print("The result is: ", substraction(operand1, operand2))
    elif operator == '*':
        print("The result is: ", multiplication(operand1, operand2))
    elif operator == '/':
        print("The result is: ", division(operand1, operand2))
    else:
        print("Invalid input. Please check the options again!")
except ValueError:
    print("Please enter numbers only!")