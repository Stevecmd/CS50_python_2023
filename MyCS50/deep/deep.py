# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two
# or forty two. Otherwise output No.

def main():
    question = answer(str(input("What is the Answer to the Great Question Of Life, the Universe and Everything? ").lower().strip()))


def answer(d):
    if d == ("42"):
        print("Yes")

    elif d == ("forty-two"):
        print("Yes")

    elif d == ("forty two"):
        print("Yes")

    elif d == ("forty two"):
        print("Yes")

    elif d == ("forty two"):
        print("Yes")

    else:
        print("No")

main()

# Be sure to vary the casing of your input and “accidentally” add spaces on either side of your input before pressing enter.
# Your program should behave as expected, case- and space-insensitively.