import random

def main():
    level = get_level()  # Get the level from the user input

    score = 0  # Initialize the user's score
    for _ in range(10):  # Loop 10 times for 10 math problems
        # The underscore (_) is a conventional placeholder that
        # signifies we don't care about the actual loop counter's value;
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 3  # 3 tries maximum for each problem
        while tries > 0:
            answer = input(f"{x} + {y} = ")

            # Check if the user's answer is a number and is correct
            if answer.isdigit() and int(answer) == x + y:
                score += 1  # Increment the score
                break  # Move on to the next problem
            else:
                tries -= 1  # Decrement the tries for every wrong answer
                if tries == 0:  # No more tries left
                    print(f"The correct answer is {x + y}.")
                else:
                    print("EEE")  # Error message

    # Print the user's final score
    # print(f"Your final score is {score} out of 10.")
    print(score)

def get_level():
    while True:
        level = input("Level: ")

        if level in ["1", "2", "3"]:  # Define list to check if level is one of the valid choices
            return int(level)
        else:
            print("Please enter a valid number for the level: 1, 2, or 3.")

def generate_integer(level): # We are defining the parameters for the different levels
    if level == 1:
        return random.randint(0, 9)  # Random number with 1 digit
    elif level == 2:
        return random.randint(10, 99)  # Random number with at least 2 digits
    elif level == 3:
        return random.randint(100, 999)  # Random number with at least 3 digits
    else:
        raise ValueError("Level should be 1, 2, or 3.")

if __name__ == "__main__":
    main()