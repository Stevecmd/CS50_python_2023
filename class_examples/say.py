#!/usr/bin/env python3
# The above line ensures that we are using python3

# On a new terminal run 'pip install cowsay' to run the program
# sudo pip install cowsay

# import cow_says as cow_says
# import sys

# if len(sys.argv) == 2:
#     cow_says.cow("hello, " + sys.argv[1])


import cowsay as cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    # cowsay.dragon("Hello from the dragon too!")
    cowsay.trex("Hello from the dragon too!")


