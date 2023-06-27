import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.csv'):
    sys.exit(f'{sys.argv[1]} is not a valid CSV file')

if not sys.argv[2].endswith('.csv'):
    sys.exit(f'{sys.argv[2]} is not a valid CSV file')

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        print(reader)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
else:
    with open(sys.argv[2], "a") as file:
        writer = csv.Dict