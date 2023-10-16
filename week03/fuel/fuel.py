def main():
    get_fuel()

def get_fuel():
    while True:
        x = input("Enter a fraction in the format X/Y (or 'quit' to stop): ")
        if x.lower() == 'quit':
            break
        try:
            numerator, denominator = map(int, x.split('/'))
            percentage = round((numerator / denominator) * 100)
            if percentage == 0:
                # percentage = 'E'
                print("E")
                return ("E")
            if percentage == 1:
                # percentage = 'E'
                print("E")
                return ("E")
            elif percentage == 100:
                # percentage = 'F'
                print("F")
                return ("F")
            elif percentage == 99:
                # percentage = 'F'
                print("F")
                return ("F")
            elif percentage > 100:
                percentage = 'F'
                print("Invalid: Cannot go beyond 100%. Please try again")
                get_fuel()
            print(f"{percentage}%")
            return x
        except ValueError:
            print("Please enter a valid fraction in the format X/Y.")
            pass
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please enter a valid fraction.")
            pass
main()

# Explanation:
# the main() function calls get_fuel(), and inside get_fuel(),
# the program continues to prompt the user for a fraction until 'quit' is entered.
# It then calculates and prints the equivalent percentage for each valid fraction entered.
# If the user enters an invalid fraction or a fraction with a zero denominator,
# the program informs the user of the error and then asks for a new input.