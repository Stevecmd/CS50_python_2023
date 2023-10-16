def main():
    x = int(input("What is x? "))
    if is_even(x):
        print(f"The number {x} is Even.")
    else:
        print(f"The number {x} is Odd.")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()


# Pythonic code alternatives
# 1.
# return True if n % 2 == 0 else False
# 2.
# return n % 2 == 0

# match in python aka switch in other languages