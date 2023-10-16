# Run
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
# unzip muppets.zip
# Install the Pillow library: pip install Pillow
import sys
from PIL import Image, ImageOps

def main():
    check_command_line_args()
    # Read the image provided by the user and overlay a shirt on it
    result_image = read_and_overlay_shirt(sys.argv[1])
    # Save the resulting image to the path specified by the user
    result_image.save(sys.argv[2])

def check_command_line_args():
    # Checking if the number of command-line arguments is less than or equal to 2
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")

    # If the number of arguments is not equal to 3, the user provided incorrect arguments
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")

    # If the number of command-line arguments is 4 or more there is an issue
    if len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")

    # Extracting file extensions from the input and output file names
    input_extension = sys.argv[1].split('.')[-1].lower()
    output_extension = sys.argv[2].split('.')[-1].lower()

    # A list of valid file extensions as per the question
    valid_extensions = ['jpg', 'jpeg', 'png']

    # Checking validity of input and output file extensions as per list above
    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        sys.exit("Invalid output")

    # Checking validity of input and output file extensions, must be similar
    if input_extension != output_extension:
        sys.exit("Input and output have different extension")

    # Checking if the specified input file exists; if not, exit the program
    try:
        with open(sys.argv[1], "rb"):
            pass
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

def read_and_overlay_shirt(input_path):
    # Open the shirt image
    shirt = Image.open("shirt.png")
    # Open the input image provided by the user
    input_image = Image.open(input_path)
    # Resize and crop the input image to match the shirt image's size
    resized_input = ImageOps.fit(input_image, shirt.size)
    # Overlay the shirt image on the resized input image
    resized_input.paste(shirt, (0, 0), shirt)  # Use shirt as a mask for transparency
    # Return the processed image
    return resized_input

if __name__ == "__main__":
    main()
