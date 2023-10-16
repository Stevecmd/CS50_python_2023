# start with pip install pyfiglet
import sys
import random # To be used where user inputs zero to get a random font
# imorting the Figlet module from pyfiglet
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Get the list of available fonts from the pyfiglet
    fonts = figlet.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1: # checks if the script was called without any additional command-line arguments (other than the script name itself)
        selected_font = random.choice(fonts)  # Selects a random font to be applied
    elif len(sys.argv) == 3: # Positions on command line 0: script itself 1: -f and 2: --font
        if sys.argv[1] in ['-f', '--font']:
            if sys.argv[2] in fonts:
                selected_font = sys.argv[2]
            else:
                # sys.exit(f"Error: {sys.argv[2]} is not a valid font name.")
                sys.exit(f"Invalid usage")
        else:
            sys.exit(f"Error: {sys.argv[1]} is not a recognized option. Use -f or --font to specify a font.")
    else:
        sys.exit("Invalid usage")

    # Set the font
    figlet.setFont(font=selected_font)

    # Prompt the user for text
    text = input("Enter the text: ")

    # Output the text in the desired font
    print(figlet.renderText(text))

# Running the script directly and not as a module
# If script is imported into another program, this main wont be imported
# hence a clash is avoided esp if the other program has its own main
if __name__ == '__main__':
    main()


