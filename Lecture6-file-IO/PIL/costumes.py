import sys

form PIL import Image

images = []

# take the cmd line arguments, but skip the first (program name)
for arg in sys.argv[1:]:
    image = Image.open(arg)