import sys

count = 0

if len(argv < 2):
    sys.exit('Too few command-line arguments')

if len(argv > 2):
    sys.exit('Too many command-line arguments')

if not argv[1].endswith('.py'):
    sys.exit('Not a Python file')

with open('sample.py') as file:
    for line in file:
        if not line.startswith('#') and line.strip() != "":
            print('start' + line + 'end')
            count += 1

print(count)