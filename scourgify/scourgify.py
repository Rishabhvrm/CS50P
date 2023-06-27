import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')


try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(reader)

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')