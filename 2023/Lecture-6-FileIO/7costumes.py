# Images
# PIL - Python Image Library
# pillow.readthedocs.io

import sys

from PIL import Image

images = ['https://www.shutterstock.com/image-photo/young-woman-canoeing-lake-bohinj-on-1494248774',
          'https://www.shutterstock.com/image-photo/multiracial-male-female-friends-standing-talking-2268291185']

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "img1.gif", save_all=True,
    append_images=[images[1]], duration=200, loop=0
)