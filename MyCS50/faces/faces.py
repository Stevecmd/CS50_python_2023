# In a file called faces.py, implement a function called convert that accepts a str as input
# and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face)
# and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

# Then, in that same file, implement a function called main that prompts the user for input,
# calls convert on that input, and prints the result. You’re welcome,
# but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
# Be sure to call main at the bottom of your file.

# def main():
#     print("input can only be \":)\" or \":(\"")
#     x = str(input("What's the value of string x? "))
#     print("x smiley face is", convert(x))

# def convert(n):
#     if n == ":)":
#         return "🙂"
#     if n == ":(":
#         return "🙁"

# main()

def main():
    print("input can contain \":)\" or \":(\" anywhere")
    x = str(input("What's the value of string x? "))
    print (convert(x))

def convert(n):
    n = n.replace(":)", "🙂")
    n = n.replace(":(", "🙁")
    return n

main()

