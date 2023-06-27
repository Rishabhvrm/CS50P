import sys
import csv
from tabulate import tabulate

# cmd line argument checks
if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')

pizza_row = []

with open(sys.argv[1]) as file:
    try:
        reader = csv.reader(file)
        for pizza, small, large in reader:
            row = []
            row.append(pizza)
            row.append(small)
            row.append(large)
            pizza_row.append(row)
            # print(pizza_row)
            # print(tabulate(table, headers, tablefmt='plain'))
    except FileNotFoundError:
        sys.exit('File does not exist')
    else:
        headers = pizza_row[0]
        table = pizza_row[1:]
        print(tabulate(table, headers, tablefmt="grid"))