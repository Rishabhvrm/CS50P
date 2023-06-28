import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')


try:
    _, extension1 = sys.argv[1].split('.')
    __, extension2 = sys.argv[1].split('.')
except:
    sys.exit('Invalid output')
else:
    valid_extensions = []
    if extension1 not in valid_extensions or extension2 not in valid_extension:
        sys.exit('')
    if extension1 != extension2:
        sys.exit('Input and output have different extensions')