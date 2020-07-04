'''Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?'''

class Customer:

    def __init__(self, account_name, account_number, balance, contact_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.contact_number = contact_number

    
    def customer_info(self, ID):
        return self.account_name, self.account_number, self.balance, self.contact_number

    def deposit(self, amount):
        self.balance += amount
        print(f"Successful deposit of Rs.{amount} \n")
        print(f"Current balance is Rs.{self.balance} \n")


    def withdraw_money(self, amount):
        minimum_balance = 5000
        minimum_balance = int(minimum_balance)
        print(f"Your current balance is Rs.{self.balance} \n")
        
        if self.balance < amount:
            print("You do not have enough balance. \n")

        elif (self.balance - amount) < minimum_balance:
                print("You are trying to withdraw too much. \n")

        else:
            self.balance -= amount
            print(f"You had successful withdrawl of Rs.{amount}. \n")
            print(f"Current balance is Rs.{self.balance} \n")



customer1 = Customer("Ram KC", 1987, 50000, 9841000000)            

account_name, account_number, balance, contact_number = customer1.customer_info(1)

print("Information: \n \n" f"Name : {account_name},", f"Account no.: {account_number},", f"Balance : Rs.{balance},", f"Contact no.: {contact_number}" "\n")

customer1.deposit(5000)
customer1.withdraw_money(50000)
