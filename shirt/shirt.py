import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments ')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')



_, extension1 = sys.argv[1].split('.')
__, extension2 = sys.argv[1].split('.')

if extension1 != extension2:
    sys.exit('Input and output have different extensions')