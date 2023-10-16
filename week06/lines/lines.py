import sys # Access command line arguments

def main():
    # Check command line arguments
    check_command_line_args()
    # Try except loop
    try:
        file = open(sys.argv[1], "r") # open the file and read it
        filevariable = file.readlines()
    # File doesnt exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Use a loop to implement check_space_and_starts on every row
    number_of_rows = 0 # starting the row count
    for row in filevariable:
        if check_space_and_starts(row) == False:
            number_of_rows += 1 # Add a count
    print(number_of_rows) # print the total number of rows

def check_command_line_args():
    # Check the number of elements given on the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if the file has a .py extension
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    # print(sys.argv)

def check_space_and_starts(row):
    if row.isspace(): # python function to check spaces
        return True
    if row.lstrip().startswith('#'): # strip extra spaces and check if the line starts with #
        return True
    # If either of the above checks fails
    return False

if __name__ == "__main__":
    main()