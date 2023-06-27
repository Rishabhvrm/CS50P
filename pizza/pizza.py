import sys
import csv

# cmd line argument checks
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')

with open(sys.argv[1]) as file:
    try:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
    except FileNotFoundError:
        sys.exit('File does not exist')