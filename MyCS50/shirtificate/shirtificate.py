# Run
# wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
# pip install fpdf2 Pillow
# pip install fpdf

# Code version 1 - Works
from fpdf import FPDF
from PIL import Image

def main():
    name = input("Enter your name: ")
    generate_shirtificate(name)

def generate_shirtificate(name):
    # Creating a new PDF in portrait mode and in A4 format
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Adding a new page
    pdf.add_page()

    # Setting the title font
    pdf.set_font("helvetica", size=42)
    pdf.set_xy(0, 20)  # Moving down a bit for better positioning
    pdf.multi_cell(210, 20, "CS50 Shirtificate", 0, "C")  # 210mm is A4 width, centered text

    # Placing the shirt image
    shirt_path = "shirtificate.png"
    img = Image.open(shirt_path)

    # Scale image to fit A4 while maintaining aspect ratio
    aspect_ratio = img.width / img.height
    img_width_mm = 210  # Maximum width for A4 in mm
    img_height_mm = img_width_mm / aspect_ratio

    # If height exceeds A4 height after scaling, adjust it
    if img_height_mm > 277:  # 277mm to account for some margins
        img_height_mm = 277
        img_width_mm = img_height_mm * aspect_ratio

    # Calculating the position to center the image on the paper
    x_centered = (210 - img_width_mm) / 2  # 210mm is A4 width
    y_centered = (297 - img_height_mm) / 2  # 297mm is A4 height

    pdf.image(shirt_path, x=x_centered, y=y_centered, w=img_width_mm, h=img_height_mm)

    # Printing the user's name on the shirt image in white text as per instructions
    statement = f"{name} took CS50"

    text_height = 10
    vertical_center = y_centered + (img_height_mm / 2)
    adjusted_y = vertical_center - (text_height / 2)

    pdf.set_xy(x_centered, adjusted_y)
    pdf.set_text_color(255, 255, 255)  # white in RGB
    pdf.set_font("helvetica", size=24)
    pdf.multi_cell(img_width_mm, text_height, statement, 0, "C")  # Centering the text

    # Saving the PDF file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()