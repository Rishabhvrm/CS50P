import sys
from PIL import Image
from PIL import ImageOps

def main():
    validations()
    images = []

    try:
        for arg in sys.argv[1:]:
            # image = Image.open(arg)
            images.append(arg)

        muppet = Image.open(sys.argv[1])
        shirt = Image.open('shirt.png')

        muppet_size = muppet.size
        shirt_size = shirt.size

        # resize input to the size of shirt
        ImageOps.fit(muppet, muppet_size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        # muppet.paste(shirt, box=None, mask=shirt)
        muppet.paste(shirt, shirt)
        muppet.save('after4.jpg')
    except FileNotFoundError:
        sys.exit('Input does not exist')


def validations():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments ')

    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    try:
        _, extension1 = sys.argv[1].split('.')
        __, extension2 = sys.argv[2].split('.')
    except:
        sys.exit('Invalid output')                      # if filename does not have '.'
    else:
        valid_extension = ['jpg', 'jpeg', 'png']
        if extension1 not in valid_extension:
            sys.exit('Invalid input')
        if extension2 not in valid_extension:
            sys.exit('Invalid output')
        if extension1 != extension2:
            sys.exit('Input and output have different extensions')

main()