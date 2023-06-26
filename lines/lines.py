import sys

count = 0

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.py'):
    sys.exit('Not a Python file')


try:
    with open('sample.py') as file:
        print(line)
except FileNotFoundError:
    sys.exit('File does not exist')
else:
    for line in file:
        if not line.startswith('#') and line.strip() != "":
            print('start' + line + 'end')
            count += 1


print(count)