from budget import Budget

def updateFood():
     with open("food.txt", "w") as foodfile:
            foodfile.write(str(food.balance))

def updateBills():
    with open("bills.txt", "w") as foodfile:
                foodfile.write(str(bills.balance))
 
with open("food.txt", "r") as file1:
    var1 = int(file1.read())

food = Budget(var1)

with open("bills.txt", "r") as file1:
    var1 = int(file1.read())

bills = Budget(var1)

running = True

while running:
    control = input("1: edit budget")
    if control == "1":
        food.deposit(bills.withdraw(45))
        updateFood()
        updateBills()
    elif control == "0":
        running = False
