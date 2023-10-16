# # Soln 1
# import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# Soln 2
# from random import choice
# coin = choice(["Heads", "Tails"])
# print(coin)

# Soln 3
# Print a number between in the range a - b inclusive
# # random.randint(a, b)
# import random
# number = random.randint(1, 3)
# print(number)

# Soln 4
# Randomly print the value of items stored in a list
# # random.shuffle(x)
import random

cards = ['jack', 'queen', 'king', 'Ace']
random.shuffle(cards)
for card in cards:
    print(card)