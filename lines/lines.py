import sys

count = 0

if len(argv > 2):
    

if not argv[1].endswith('.py'):
    sys.exit('Not a Python file')

with open('sample.py') as file:
    for line in file:
        if not line.startswith('#') and line.strip() != "":
            print('start' + line + 'end')
            count += 1

print(count)