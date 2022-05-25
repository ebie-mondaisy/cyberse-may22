# books={"Writer":["Book 1", "Book 2", "Book 3", "Book 6"], "Author":["Book 20", "Book 23"], "Pen Holder":["Book 67", "Book 9", "Book 45"]}

# bookName = input("Enter Author Name: ")

# print(f"Results for {bookName}: " + "\n" .join(books[bookName]))

# markInput = int(input("Enter mark: "))

# #if markInput >= 85:
# #    print("Distinction")
# #elif markInput >= 65:
# #    print("Pass")
# #else:
# #    print("Fail")

# if markInput >= 65:
#     if markInput >= 85:
#         print("Distinction")
#     else:
#         print("Pass")
# else:
#     print("Fail")

# count = 0
# name = str(input("What is your name? -->"))

# while count < 5:
#     print(name, "is awesome!")
#     count += 1

#ask for a name 5 times
count = 0

while count < 5:
    name = str(input("What is your name? -->"))
    print(name, "is awesome!")
    count += 1