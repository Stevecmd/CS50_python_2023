import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regex to find all case-insensitive occurrences of 'um' as a standalone word
    matches = re.findall(r'\bUM\b', s, re.IGNORECASE)
    # Getting the length of matches
    return len(matches)

if __name__ == "__main__":
    main()
