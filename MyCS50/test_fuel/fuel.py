def main():
    fraction = get_fuel()
    if fraction:  # Ensure fraction is not None before continuing
        percentage = convert(fraction)
        gauge(percentage)

def get_fuel(): # Obtain a fraction from the user using
    while True:
        fraction = input("Enter a fraction in the format X/Y (or 'quit' to stop): ") # Accept user input as a fraction
        if fraction.lower() == 'quit': # If the user types quit, the function returns None (terminating the input loop).
            return None
        try:
            numerator, denominator = map(int, fraction.split('/')) # Splitting the numerator and denominator
            if denominator == 0:
                raise ZeroDivisionError
            return fraction
        except ValueError:
            print("Please enter a valid fraction in the format X/Y.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a valid fraction.")

def convert(fraction): # Convert the fraction to a percentage
    try:
        numerator, denominator = map(int, fraction.split('/')) # Splitting the numerator and denominator
        if numerator > denominator:
            raise ValueError("Numerator is greater than denominator.")
        percentage = round((numerator / denominator) * 100)
        return percentage
    except ZeroDivisionError:
        print("Denominator cannot be zero. Please enter a valid fraction.")
        raise
    except ValueError:
        print("Please enter a valid fraction in the format X/Y.")
        raise ValueError("Please enter a valid fraction in the format X/Y.")

# def convert(fraction):
#     try:
#         numerator, denominator = map(int, fraction.split('/'))
#         if numerator > denominator:
#             raise ValueError("Numerator is greater than denominator.")
#         percentage = round((numerator / denominator) * 100)
#         return percentage
#     except ZeroDivisionError:
#         print("Denominator cannot be zero. Please enter a valid fraction.")
#         raise
#     except ValueError as e:
#         print(e)
#         raise


def gauge(percentage): # Determine and display the category of the percentage
    if percentage <= 0:
        print("E")
        return "E"
    elif percentage == 1:
        print("E")
        return "E"
    elif percentage >= 99:
        print("F")
        return "F"
    else:
        print(f"{percentage}%")
        return f"{percentage}%"

if __name__ == "__main__":
    main()


# Explanation:
# the main() function calls get_fuel(), and inside get_fuel(),
# the program continues to prompt the user for a fraction until 'quit' is entered.
# It then calculates and prints the equivalent percentage for each valid fraction entered.
# If the user enters an invalid fraction or a fraction with a zero denominator,
# the program informs the user of the error and then asks for a new input.