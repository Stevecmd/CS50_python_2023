# Version 1 - Submitted
def main():
    emojize = str(input("Please type in the emoji? "))
    result = hello(emojize)
    print(f"Output: {result}")

def hello(input_str):
    emoji_map = {
        ":1st_place_medal:": "🥇",
        ":2nd_place_medal:": "🥈",
        ":3rd_place_medal:": "🥉",
        ":money_bag:": "💰",
        ":smile_cat:": "😸",
        ":candy:": "🍬",
        # Add more mappings as needed
    }

    return emoji_map.get(input_str, "Unknown emoji")

if __name__ == "__main__":
    main()


# Version 2
# Run: pip install emoji
# By installing the emoji library, we have access to more emoji's

# import emoji

# def main():
#     emojize = input("Please type in the emoji code (e.g., :1st_place_medal:): ")
#     result = emojize_string(emojize)
#     if result == emojize:  # Check if the input wasn't converted, meaning it might not be recognized
#         print("Unknown emoji code!")
#     else:
#         print(f"Output: {result}")

# def emojize_string(input_str):
#     return emoji.emojize(input_str)  # Removed use_aliases

# if __name__ == "__main__":
#     main()

# Version 3 - prints strings with emoji from a dictionary
# def main():
#     user_input = input("Please type in the text with emoji codes: ")
#     result = convert_emojis(user_input) # Applying the swap function to the input
#     print(f"Output: {result}") # Shows the transformed sentence

# def convert_emojis(input_str):
#     emoji_map = {
#         ":1st_place_medal:": "🥇",
#         ":2nd_place_medal:": "🥈",
#         ":3rd_place_medal:": "🥉",
#         ":money_bag:": "💰",
#         ":smile_cat:": "😸",
#         ":candy:": "🍬",
#         # Add more mappings as needed
#     }

#     words = input_str.split()  # Split the input string by spaces into words
#     for index, word in enumerate(words):
#         # Check if the word is a key in our emoji_map
#         if word in emoji_map:
#             words[index] = emoji_map[word]  # Replace with the corresponding emoji

#     return ' '.join(words)  # Join the words back into a single string

# if __name__ == "__main__":
#     main()

