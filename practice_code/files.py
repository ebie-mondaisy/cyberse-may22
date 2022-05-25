#different way of executing the same function as the one above ^^^
'''Create a Python file which does the following:

Opens a new text file called "teams.txt" and adds the names of 5 sports teams.
Reads and displays the names of the 1st and 4th team in the file.
'''
# with open("teams.txt", "w") as file1:
#     sports = "London Spitfire\n" + "San Fransico Shock\n" + "Florida Mayhem\n" + "Houston Outlaws\n" + "Seoul Dynasty"
#     file1.write(sports)

# file1 = open("teams.txt", "r")
# print(file1.readline())
# file1.seek(50)
# print(file1.readline())

# file1.close()

#####trainer solution 
# with open("teams.txt", "w") as file1:
#     file1.write("Team1\nTeam2\nTeam3\nTeam4\nTeam5")

# with open("teams.txt", "r") as file1:
#     list1 = file1.readlines()

# for line in list1:
#     if list1.index(line) == 0 or list1.index(line) == 3
#         print(line)

'''Create a new Python file which does the following:

Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
Print out the edited file line by line.
'''
# file = open("teams.txt", "r")

# lines = file.readlines()
# lines[0] = "This is a new line\n"

# file = open("teams.txt", "w")
# file.writelines(lines)
# file.close()

file = open("teams.txt", "r")
lines = file.read()
print(lines)
file.close()

#######trainer solution

# with open("teams.txt", "r") as file1:
#     list1 = file1.readlines()

# with open("teams.txt", "w") as file1:
#     for line in list1:
#         if list1.index(line) == 0:
#             file.write()

# with open("teams.txt", "r") as file1:
#     list1 = file1.readlines()

# for line in list1:
#     print(line)