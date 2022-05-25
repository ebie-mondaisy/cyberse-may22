from random import choice
from math import ceil
from flask import Flask

# ceil - rounds up
# round - rounds down

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = round(choice(list1) / 2)
print(answer)
print(ceil(answer))