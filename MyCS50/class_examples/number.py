# Solution 1
# try:
#     x = int(input("What is x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# Solution 2
# Handles the error better by not stopping at error and also printing it
# Else is executed only if try worked
# try:
#     x = int(input("What is x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# Solution 3
# We are using a loop to catch all errors and ask for better input
# Instead of code terminating, user gets the chance to try again
# However the program may run infinitely
# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

# Solution 4
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x # return can break out of a loop and also give output
# main()

# Solution 5
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#             return x
#         except ValueError:
#             print("x is not an integer")
# main()

# Solution 6
# pass is used to catch the error but not take further action
# The loop will restart until correct input is given
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#             return x
#         except ValueError:
#             pass
# main()


# Solution 7
# We can let the function expect a named variable such as 'prompt'
# and use 'prompt' in the body
# the code is more reusable this way
# the function get_int only needs to know the value returned as 'prompt'
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
main()