from budget import Budget

food = Budget(500)
with open("food.txt", "w") as foodfile:
    foodfile.write(str(food.balance))

bills = Budget(350)
with open("bills.txt", "w") as foodfile:
    foodfile.write(str(bills.balance))

# the attribute it calling to the same class. so it will identify what the output needs to be
# methods can access each other while being within themselves
print(food.deposit(bills.withdraw(45)))
with open("food.txt", "w") as foodfile:
    foodfile.write(str(food.balance))
with open("bills.txt", "w") as foodfile:
    foodfile.write(str(bills.balance))

#print(bills.withdraw(23))
print("Food - " + str(food))
print("Bills - " + str(bills))