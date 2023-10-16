def main():
    fruits = {'apple': 130, 'avocado': 50, 'sweet cherries': 100, 'kiwifruit': 90, 'pear': 100} #dictionary with key: value pairs
    while True:
        fruit_name = str(input("Enter a fruit name (or 'quit' to stop): ").lower())
        if fruit_name == 'quit': # Exit loop
            break
        elif fruit_name not in fruits: # Checking if fruit in DB
            print("This fruit is not in our database.")
        else:
            calories = get_calories(fruit_name, fruits)
            print(f"Calories: {calories}")

def get_calories(fruit, fruits_dict):
    return fruits_dict.get(fruit, None)

main()

# Code breakdown

# fruits = {'apple': 130, 'avocado': 50, 'sweet cherries': 100, 'kiwifruit': 90, 'pear': 100}:
# This line defines a dictionary where each key-value pair is a fruit's name
# and its associated calorie count.
# Notice the change from string values to integer values for the calorie counts,
# which is more appropriate for numeric data.

# The while True: loop allows the program to run indefinitely until the user decides to quit.
# This is more user-friendly as it lets users check calories for multiple fruits without
# needing to restart the program each time.

# fruit_name = str(input("Enter a fruit name (or 'quit' to stop): ").lower()):
# This line prompts the user for input, converting the input to lowercase.
# If the user enters "quit", the program will terminate.

# if fruit_name == 'quit': break: If the user inputs 'quit',
# this code breaks out of the while loop, effectively ending the program.

# elif fruit_name not in fruits: print("This fruit is not in our database."):
# If the entered fruit's name is not present in the dictionary, the program now
# gives an informative message that the fruit is not in its database.

# else: calories = get_calories(fruit_name, fruits) print(f"Calories: {calories}"):
# If the fruit's name is found in the dictionary, the program fetches the corresponding
# calorie count and prints it.

# def get_calories(fruit, fruits_dict): return fruits_dict.get(fruit, None):
# This function returns the calorie count of the specified fruit from the given dictionary.
# If the fruit is not found in the dictionary, it returns None. However, with the updated code,
# the situation where None is returned should no longer occur,
# given the earlier check (elif fruit_name not in fruits).

# main(): This calls the main function to start the execution of the program.