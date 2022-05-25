
# class Category:

#     def __init__(self, name):
#         self.name = name
#         self.ledger = list()

#     def deposit(self, amount, description=""):
#         self.ledger.append({"amount": amount, "description": description})

#     def withdraw(self, amount, description=""):
#         if(self.check_funds(amount)):
#             self.ledger.append({"amount": -amount, "description": description})
#             return True;
#         return False
    
#     def get_balance(self):
#         total_cash = 0
#         for item in self.ledger:
#             total_cash += item["amount"]

#         return total_cash

#     def transfer(self, amount, category):

#         if(self.check_funds(amount)):
#             self.withdraw(amount, "Transfer to " + category.name)
#             category.deposit(amount, "Transfer from " + self.name)
#             return True
#         return False
#     def check_funds(self, amount):
#         if(self.get_balance() >= amount):
#             return True
#         return False

class Budget():
    def __init__(self, balance):
        self.balance = balance

    #use this object to output the right/required information
    def __repr__(self):
        return f"The current balance of this budget is: {self.balance}"

    def withdraw(self, amount):
        self.balance -= amount
        return amount

    def deposit(self, amount):
        self.balance += amount
        return amount

     