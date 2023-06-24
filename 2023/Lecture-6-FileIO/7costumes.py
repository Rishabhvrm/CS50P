# Images
# PIL - Python Image Library
# pillow.readthedocs.io

import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "img1", save
)