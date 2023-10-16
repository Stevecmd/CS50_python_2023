# Soln 1
# name = input("What's your name? ")
# print(f"hello, {name}")

# Soln 2
# names = [] # empty list

# for _ in range(3):
#     name = input("What's your name? ") # Getting the names
#     names.append(name) # Append each entry to the names list
#     print(f"hello, {name}")

# Soln 3
# names = [] # empty list

# for _ in range(3):
#     names.append(input("What's your name? ")) # Append each entry to the names list

# for name in sorted(names): # sort the entries alphabetically
#     print(f"hello, {name}")

# # Soln 4: Saving the name to a file but overwrites previous data
# name = input("What's your name? ")

# file = open("names.txt", "w") # opens a file and w to write in it
# file.write(name) # write is a method that comes from file so we will write name to it
# file.close() # saving and closing the file we were editing
# # run code names.txt to see file contents

# # Soln 5: Saving the name to a file but appends to previous data
# name = input("What's your name? ")

# file = open("names.txt", "a") # opens a file and a to append in it
# file.write(name) # write is a method that comes from file so we will write name to it
# file.close() # saving and closing the file we were editing
# # run code names.txt to see file contents

# # Soln 6: Saving the name to a file on a separate line
# name = input("What's your name? ")

# file = open("names.txt", "a") # opens a file and a to append in it
# file.write(f"{name}\n") # write is a method that comes from file so we will write name to it
# file.close() # saving and closing the file we were editing
# # run code names.txt to see file contents

# # Soln 7: Saving the name to a file on a separate line
# name = input("What's your name? ")

# with open("names.txt", "a") as file: # with (name of function) as (name of variable to be assigned return value of open)
#     file.write(f"{name}\n") # write is a method that comes from file so we will write name to it
# # run code names.txt to see file contents
# # file closes before any code below is processed

# # Soln 8: Reading contents of the file
# with open("names.txt", "r") as file: # r = read
#     for line in file:
#         print("Hello,", line.rstrip()) # strip removes the auto new line on each line
# # run code names.txt to see file contents

# Soln 9: Reading contents of the file and sorting
# names = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("names.txt") as file: # r = read but its default
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names): # sort the names that are in memory and print in order
#     print(f"Hello, {name}!")

# # Soln 10: Reading contents of the file and sorting
# names = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("names.txt") as file: # r = read but its default
#     for line in sorted(file): # sort the names that are in memory and print in order
#         print(f"Hello,",line.rstrip(),"!")

# Soln 11: Reading contents of the file and sorting(reverse)
names = [] # list to gather data
# iterate over the file contents and stripping right space
with open("names.txt") as file: # r = read but its default
    for line in sorted(file, reverse=True): # sort the names that are in memory and print in order
        print(f"Hello,",line.rstrip(),"!")
