# # Solution 1
# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print ("Valid")
# else:
#     print ("Invalid")

# # Solution 2
# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and "." in domain:
#     print ("Valid")
# else:
#     print ("Invalid")

# # Solution 3
# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and "." in domain.endswith(".edu"):
#     print ("Valid")
# else:
#     print ("Invalid")

# Notes
# . - any character except a new line
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetitions
# {m} - m repetitions
# {m, n} - m - n repetitions
# ^ matches the start of a string
# $ matches the end of a string or just before the newline at the end of the string
# [] set of characters
# [^] complimenting the set - do not match any of the characters

# # Solution 5
# import re

# email = input("What's your email? ").strip()

# if re.search(".*@.*", email): # Checks for data to the left or right of @
#     print("Valid")
# else
#     print("Invalid")

# # Solution 6
# import re

# email = input("What's your email? ").strip()

# if re.search(".+@.+", email): # Checks for data to the left and right of @
#     print("Valid")
# else
#     print("Invalid")

# # # Solution 7
# import re

# email = input("What's your email? ").strip()

# if re.search(r".+@.+\.edu", email): # Specifically makes sure address ends with .edu
#     print("Valid") # The \ above is used as an escape character
# else
#     print("Invalid") # r is used to pass the string exactly as is

# # Solution 7
# import re

# email = input("What's your email? ").strip()

# if re.search(r"^[^@]+@[^@]+\.edu$", email): # [^@] - any character except @ sign
#     print("Valid") # The \ above is used as an escape character
# else
#     print("Invalid")

# # Solution 8
# import re

# email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else
#     print("Invalid")

# # # Solution 8
# import re

# email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.edu$", email): # \w any alphanumeric character
#     print("Valid")
# else
#     print("Invalid")

# Notes 2
# \d - decimal digit
# \D - not a decimal digit
# \s - whitespace characters
# \S - not a whitespace character
# \w - word character as well as numbers and underscore
# \W - not a word character

# # Solution 9
# import re

# email = input("What's your email? ").strip()

# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): # See re.IGNORECASE, re.MULTILINE, re.DOTALL
#     print("Valid")
# else:
#     print("Invalid")

# # Solution 10
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # See re.IGNORECASE, re.MULTILINE, re.DOTALL
    print("Valid")
else:
    print("Invalid")


# Notes.
# The regular expression part: re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):

# - ^: Asserts the start of a line.
# - \w+: Matches one or more word characters (equivalent to [a-zA-Z0-9_]).
# - @: Matches the literal "@" character.
# - (\w+\.)?: Matches one or more word characters followed by a period. The ? means that this entire group is optional.
# - \w+: Matches one or more word characters again.
# - \.edu: Matches a period followed by "edu".
# - $: Asserts the end of a line.
# The r before the string indicates that it's a raw string, which means backslashes will be treated
# as literal backslashes and not escape characters.
# re.IGNORECASE: This is a flag that makes the regex pattern case-insensitive, meaning
# it will match both "EDU" and "edu", for example.
# Overall, the pattern checks for an email that:

# Starts with one or more word characters.
# Followed by an "@".
# Optionally has one set of word characters followed by a period.
# Ends with word characters followed by ".edu".
# if re.search(...):

# If the regular expression finds a match in the provided email string,
#  it will return a match object; otherwise, it returns None.
# print("Valid"): If the regex matches, the program prints "Valid".

# else: If the regex does not match, the program goes to the else block.

# print("Invalid"): If the email doesn't match the regex, the program prints "Invalid".

# The provided comment # See re.IGNORECASE, re.MULTILINE, re.DOTALL seems to suggest
# # looking up these flags in the Python documentation to understand their behavior.
# # In this code, only re.IGNORECASE is used. The other two flags, re.MULTILINE and re.DOTALL, are not used here.


# Browsers use a cryptic form of this email address validator




