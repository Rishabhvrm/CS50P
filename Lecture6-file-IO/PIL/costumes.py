import sys

form PIL import Image

images = []

# take the cmd line arguments, but skip the first (program name)
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, appned_images=[images[1]], duration=200, loop=0
)