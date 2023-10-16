# In a file called camel.py, implement a program that prompts the user for the name of
# a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

def main():
    question = str(input("Please enter the name of a variable in camel case? ").strip())
    snake_case_name = convert(question)
    print(f"Your name in snake case is: {snake_case_name}")

def convert(x):
    result = ""
    for char in x:
        if char.isupper() and result:
            result += '_'
        result += char.lower()
    return result

main()