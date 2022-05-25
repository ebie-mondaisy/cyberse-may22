import pdb

# a = "aaa"
# b = "bbb"
# c = "ccc"

# def final (var1, var2, var3):
#     pdb.set_trace()
#     return(var1+var2+var3)

# print(final(a, b, c))

'''Exercise One: Static Debugging'''

# price = {'Burger': 10.31}
# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     print("You have enough money!")
# if item_price == user_funds:
#     print("You have the precise amount of money")
# if item_price > user_funds:
#     print("Sorry you don't have enough money")

'''Exercise Two: Static Debugging'''

# def product(n):
#     total = 1
#     for i in n:
#         total *= i
#     return total

# print(product([4,4,5]))

'''Exercise Three: dynamic Debugging'''

# def is_prime(x):

#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#             return True

'''Exercise 4: Debugging'''
#pdb.set_trace()

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n += 1
#will print the last item in the list, regardless of the number of items in the list
print (item_list[-1])