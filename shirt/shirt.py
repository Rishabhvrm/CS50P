import sys
from PIL import Image

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')


try:
    _, extension1 = sys.argv[1].split('.')
    __, extension2 = sys.argv[2].split('.')
    print(extension1, extension2)
except:
    sys.exit('Invalid output')      # if filename does not have '.'
else:
    valid_extension = ['jpg', 'jpeg', 'png']
    if extension1 not in valid_extension or extension2 not in valid_extension:
        print('------' + extension1 + '-----' + extension2)
        print(extension1 not in valid_extension)
        print(extension2 not in valid_extension)
        sys.exit('Invalid output')
    if extension1 != extension2:
        sys.exit('Input and output have different extensions')

images = []

try:
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)
except FileNotFoundError:
    sys.exit('Input does not exist')


