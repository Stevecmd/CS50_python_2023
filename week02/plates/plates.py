# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
# with your choice of letters and numbers instead of random ones.
# Among the requirements, though, are:
# 1. “All vanity plates must start with at least two letters.”
# 2. “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# 3. “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# 4. “No periods, spaces, or punctuation marks are allowed.”

# implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
# Assume that any letters in the user’s input will be uppercase.
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
# Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:  # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
        return False
    if not s[0].isalpha() or not s[1].isalpha():  # All vanity plates must start with at least two letters
        return False

    # Check if string has only letters at first then numbers
    digit_presence = False
    for char in s[2:]:  # We start checking from the third character
        if char.isnumeric():
            if char == '0' and not digit_prescence:
                return False  # The first number used cannot be a ‘0’
            digit_presence = True
        elif char.isalpha():
            if digit_presence:
                return False  # If we see a letter after seeing a digit, return False
        else:
            return False  # If character is not a letter or digit, return False, No periods, spaces, or punctuation marks are allowed.
    return True

main()

