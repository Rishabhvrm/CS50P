import sys
from PIL import Image
from PIL import ImageOps
import os

def main():
    validations()
    try:
        muppet = Image.open(sys.argv[1])            # input image
        shirt = Image.open('shirt.png')             # shirt image
    except FileNotFoundError:
        sys.exit('Input does not exist')
    else:
        shirt_size = shirt.size

        # resize input to the size of shirt
        muppet_resized_img = ImageOps.fit(muppet, shirt_size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        muppet_resized_img.paste(shirt, shirt)      # overlay shirt over muppet
        muppet_resized_img.save(sys.argv[2])        # save it


def validations():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    _, extension1 = os.path.splitext(sys.argv[1])
    try:
        _, extension1 = os.path.splitext(sys.argv[1])
        _, extension2 = os.path.splitext(sys.argv[2])
    except:
        sys.exit('Invalid output')                      # if filename does not have '.'
    else:
        valid_extension = ['.jpg', '.jpeg', '.png']
        if extension1 not in valid_extension:
            sys.exit('Invalid input')
        if extension2 not in valid_extension:
            sys.exit('Invalid output')
        if extension1 != extension2:
            sys.exit('Input and output have different extensions')

main()