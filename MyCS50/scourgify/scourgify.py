# Run: pip install tabulate
# Soln 1
# import sys # Access command line arguments
# import csv

# def main():
#     check_command_line_args()
#     # # Check if the file exists
#     check_file_exists()
#     # Read data from the 'before.csv' file
#     data = read_csv_file(sys.argv[1])
#     # Filter columns and write data to 'after.csv'
#     write_to_file(sys.argv[2], data)

# def check_command_line_args():
#     # Check the number of elements given on the command line
#     if len(sys.argv) < 3:
#         sys.exit("Too few command-line arguments")
#     if len(sys.argv) > 3:
#         sys.exit("Too many command-line arguments")
#     # Check if the files have a .csv extension
#     for arg in sys.argv[1:]:
#         if not arg.endswith(".csv"):
#             sys.exit(f"'{arg}' is not a CSV file")

# def check_file_exists():
#     # Check if the file exists
#     try:
#         with open(sys.argv[1], "r"): # open the file and read it
#             pass
#     # File doesnt exist
#     except FileNotFoundError:
#         sys.exit(f"Could not read {sys.argv[1]}")

# def split_name_and_house(entry):
#     name, house = entry
#     last, first = name.split(', ')
#     return {'first': first, 'last': last, 'house': house}

# def write_to_file(file_path, data):
#     with open(file_path, "w", newline='') as file:
#         # Specifying the headers for the CSV
#         writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

#         # Write headers and data rows
#         writer.writeheader()
#         for row in data:
#             # writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
#             writer.writerow(row)

# def read_csv_file(file_path):
#     new_data = []
#     with open(file_path, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             transformed_row = split_name_and_house((row['name'], row['house']))
#             new_data.append(transformed_row)
#     return new_data


# if __name__ == "__main__":
#     main()

# Soln 2
import sys
import csv

def main():
    check_command_line_args()
    data = read_and_transform_csv(sys.argv[1])
    write_to_file(sys.argv[2], data)

def check_command_line_args():
    if len(sys.argv) != 3:
        sys.exit("Provide exactly two arguments: <input_file.csv> <output_file.csv>")

    for arg in sys.argv[1:]:
        if not arg.endswith(".csv"):
            sys.exit(f"'{arg}' is not a CSV file")

def split_name_and_house(entry):
    name, house = entry['name'], entry['house']
    last, first = name.split(', ')
    return {'first': first, 'last': last, 'house': house}

def read_and_transform_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            return [split_name_and_house(row) for row in reader]
    except FileNotFoundError:
        sys.exit(f"Could not read {file_path}")

def write_to_file(file_path, data):
    with open(file_path, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    main()


# Download pizza menu files via:
# wget https://cs50.harvard.edu/python/2022/psets/6/scourgify/before.csv

# Run program as:
# python pizza.py sicillian.csv / regular.csv