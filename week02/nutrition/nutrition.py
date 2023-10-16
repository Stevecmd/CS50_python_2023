# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively)
# and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits,
# which is also available as text.
# Capitalization aside, assume that users will input fruits exactly as written in the poster
# (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

def main():
        fruits = {'apple': '130', 'avocado': '50', 'sweet cherries': '100', 'kiwifruit': '90', 'pear': '100'}
        fruit_name = str(input("Item: ").lower())

        if fruit_name not in fruits:
            print("")
        else:
            calories = get_calories(fruit_name, fruits)
            print(f"Calories: {calories}")

def get_calories(fruit, fruits_dict):
    return fruits_dict.get(fruit, None)

main()