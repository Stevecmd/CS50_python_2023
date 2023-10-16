import csv

name = input("What's your name? ")
home = input("Where's your home? ")

# with open("students.csv", "a") as file: # open in append mode so as to add rather than overwrite
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# Using a dictionary
# The order is not strict eg ({"home": home, "name": name})
# It will still give the correct results
with open("students.csv", "a") as file: # open in append mode so as to add rather than overwrite
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) # Declaring format in the csv file
    writer.writerow({"name": name, "home": home})