import random  # Used to generate a random number

def main():
    level = input("Please input a level: ") # Get input from the user

    while not level.isdigit() or int(level) <= 0: # Loop to check that only positive integers are accepeted
        print("Please enter a positive integer for the level.")
        level = input("Please input a level: ")

    level = int(level) # Making the input an integer
    target_number = compute(level) # Generate the random number and assign it to target_number
    # print(f"Random number between 1 and {level}: {target_number}")

    guess_game(target_number) # invoking the guess_game function and storing the random number generated

def compute(level):
    # Generating a random number between 1 and the input
    return random.randint(1, level)

def guess_game(target):
    while True:
        guess = input("Guess: ")

        # Check if the guess is a positive integer
        while not guess.isdigit() or int(guess) <= 0:
            print("Please enter a positive integer for the guess.")
            guess = input("Guess: ")

        guess = int(guess)

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    main()
