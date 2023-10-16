# # Soln 12: Using CSV
# names = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         row = line.rstrip().split(",") # split the data on each input by comma
#         print(f"{row[0]} is in {row[1]}")

# # Soln 13: Using CSV again
# names = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         name, house = line.rstrip().split(",") # split the data on each input by comma and assign to name and house respectively
#         print(f"{name} is in {house}")

# # Soln 14: Using CSV again
# students = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         name, house = line.rstrip().split(",") # split the data on each input by comma and assign to name and house respectively
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)


# # Soln 15: Sorting the printed statements by name
# students = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         name, house = line.rstrip().split(",") # split the data on each input by comma and assign to name and house respectively
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# # Soln 16: Sorting the printed statements by name simply
# students = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         name, house = line.rstrip().split(",") # split the data on each input by comma and assign to name and house respectively
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name, reverse=True): # sorting it as per the return value of get_name, can also remove reverse
#     print(f"{student['name']} is in {student['house']}")

# # Soln 17: Sorting the printed statements by name simply (refactor using an anon function: lambda function)
# students = [] # list to gather data
# # iterate over the file contents and stripping right space
# with open("students.csv") as file: # r = read but its default
#     for line in file: # sort the names that are in memory and print in order
#         name, house = line.rstrip().split(",") # split the data on each input by comma and assign to name and house respectively
#         student = {"name": name, "house": house}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"], reverse=True): # the lambda is equivalent to get_name function used previously
#     print(f"{student['name']} is in {student['house']}")

# Soln 18: Added homes to the actors and using a dictionary
# Must include row names in file
import csv
students = [] # list to gather data
# iterate over the file contents and stripping right space
with open("students.csv") as file: # r = read but its default
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})


for student in sorted(students, key=lambda student: student["name"]): # the lambda is equivalent to get_name function used previously
    print(f"{student['name']} is from {student['home']}")

# Soln 18: Added homes to the actors -- extra
# import csv

# # List to gather student data
# students = []

# # Read the CSV file and gather student data
# with open("students.csv", 'r') as file:
#     reader = csv.reader(file)

#     # Skip the header if it exists
#     next(reader, None)  # this will skip the headers, if they exist

#     for name, home in reader:
#         students.append({"name": name.strip(), "home": home.strip()})

# # Display student information, sorted by name
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")
