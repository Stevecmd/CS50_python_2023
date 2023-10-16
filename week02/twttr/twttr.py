# When texting or tweeting, it’s not uncommon to shorten words to save time or space,
# as by omitting vowels, much like Twitter was originally called twttr.
# In a file called twttr.py, implement a program that prompts the user for a str of text
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.


def main():
        VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        text = str(input("What's your string of text? ").strip())
        no_vowels = convert(text, VOWELS)
        # print(f"Your text without vowels is: {no_vowels}")
        print(f"{no_vowels}")

def convert(x, VOWELS):
    result = ""
    for char in x:
            if char not in VOWELS:
                result += char
    return result

main()