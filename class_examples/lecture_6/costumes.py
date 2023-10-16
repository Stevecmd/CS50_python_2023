# Run: python costumes.py costume1.gif costume2.gif
# then code costumes.gif
import sys # Access command line arguments
#PIL is pillow library
from PIL import Image # treat files as images

images = [] # list to accumulate all images
# iterate over list of images after adding them by using the library PIL
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Save the first image while appending other image
# Pause 200 miliseconds in between each frame and loop infinitely
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)