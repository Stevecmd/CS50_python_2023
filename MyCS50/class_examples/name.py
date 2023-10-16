# Sys stands for system
# Argv stands for argument vector - its type is list

# Soln 1
# import sys
# # In the terminal run the program and provide a sample name eg python name.py Steve
# print("Hello, my name is:", sys.argv[1])

# Soln 2
# import sys
# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Please provide your name...")

# Soln 3
# import sys
# if len(sys.argv) < 2:
#     print("Please provide your name...")
# elif len(sys.argv) > 2:
#     print("Please provide only one name...")
# else:
#     print("Hello, my name is",sys.argv[1])

# # Soln 4
# # sys.exit - enables us to exit earlier hence code improvement
# import sys
# if len(sys.argv) < 2:
#     sys.exit("Please provide your name...")
# elif len(sys.argv) > 2:
#     sys.exit("Please provide only one name...")
# else:
#     print("Hello, my name is",sys.argv[1])

# Soln 5
# slicing enables us to take in multiple inputs
import sys
if len(sys.argv) < 2:
    sys.exit("Please provide your name...")
for arg in sys.argv[1:]: # 1 is the literal start of the list. [1:5] maeans start at 1 and end at 5
    print("Hello, my name is",arg)
