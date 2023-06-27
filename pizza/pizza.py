import sys

# cmd line argument checks
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')

with open(sys.argv[1]) as file:
    