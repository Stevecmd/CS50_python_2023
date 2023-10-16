# Run: pip install tabulate

import sys # Access command line arguments
import csv
from tabulate import tabulate # prints a pretty ASCII format table

def main():
    check_command_line_args()
    # Read the CSV file and display the table
    display_csv_as_table(sys.argv[1])
    # # Check if the file exists
    try:
        file = open(sys.argv[1], "r") # open the file and read it
        pass
    # File doesnt exist
    except FileNotFoundError:
        sys.exit("File does not exist")

def display_csv_as_table(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        table = list(reader)
        headers = table[0]
        print(tabulate(table[1:], headers, tablefmt="grid"))

def check_command_line_args():
    # Check the number of elements given on the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if the file has a .csv extension
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()



# Download pizza menu files via:
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
# wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

# Run program as:
# python pizza.py sicillian.csv / regular.csv