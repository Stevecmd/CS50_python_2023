import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}!")


# if matches := re.search(r"^(.+), *(.+)$", name)::

# This line uses the walrus operator (:=) which is introduced in Python 3.8.
# It allows both assignment and checking in a single step.
# re.search(...) tries to find a pattern in the given string (name in this case).
# The regular expression pattern ^(.+), *(.+)$ works as follows:
# ^: Start of the string.
# (.+): Matches one or more of any character (except a newline) and captures it into a group (group 1).
# This is intended to capture the last name.
# , *: Matches a comma followed by zero or more spaces. This would cater to names provided as "Last,First" or "Last, First".
# (.+)$: Matches one or more of any character (except a newline) and captures it into a group (group 2).
# This is intended to capture the first name. The $ ensures the pattern matches until the end of the string.
# If the pattern is found, matches will hold the match object. If not, the expression evaluates to None, and
# the code inside the if block won't be executed.
# name = matches.group(2) + " " + matches.group(1):

# If the above pattern matches, then this line reconstructs the name in the "First Last" format.
# matches.group(2) fetches the first name (which was captured in the second group) and matches.group(1)
# fetches the last name (captured in the first group).
# print(f"Hello, {name}!"):

# This line prints a greeting using the formatted or unformatted name, depending on whether the previous reordering was executed.
# In essence, this code is made to handle name inputs like "Doe, John" and convert them to "John Doe".
# If the name is not in the "Last, First" format, it'll simply greet the name as it was provided.





