def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        # print(i, end = " ") # Debug method 1 to find the line number and the hashes printed
        # print("#" * i+1)
        print("#" * (i + 1)) # Debug: use if you want your hashes to start from 1 instead of default 0

if __name__ == "__main__":
    main()


# The function main() is defined. This function will be the main entry point of the program.

# Inside main(), the input() function is called to ask the user to enter a height for the pyramid.
# This input is then converted to an integer using int() and stored in the height variable.

# The function pyramid(height) is called with the user-provided height as its argument.

# The pyramid(n) function is defined. This function takes one argument, n, which represents the height of the pyramid.

# Inside pyramid(n), a for loop is set up to iterate n times. The variable i in the loop will range from 0 up to, but not including, n.

# For each iteration of the loop, the print() function is called to print a string of hashes (#). The number of hashes is equal to the current value of i.

# The final lines of code outside the functions (starting with if __name__ == "__main__":) make sure that the main() function will be called when this script is run directly. If this script is imported as a module into another script, the main() function will not be called.

# Please note that in the original code, the first line of the pyramid will be empty because i starts from 0 and "#" * 0 equals "" (an empty string). If you want the pyramid to start with one hash, you can modify the range(n) to range(1, n+1) in the pyramid(n) function. This will make i start from 1.