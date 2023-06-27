import csv
import sys

# checking conditions
if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

if not sys.argv[1].endswith('.csv'):
    sys.exit(f'{sys.argv[1]} is not a valid CSV file')

if not sys.argv[2].endswith('.csv'):
    sys.exit(f'{sys.argv[2]} is not a valid CSV file')

# list to store rows as dictionaries
students = []
try:
    # read from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})       # store each row as dictionary
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
else:
    # write in new file
    with open(sys.argv[2], "a") as csvfile:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for ele in students:
            last, first = ele['name'].split(', ')                                       # split first and last name
            writer.writerow({'first': first, 'last': last, 'house': ele['house']})

# -------------------------------------------------------------------------------------------------------------------------------------
# https://cs50.harvard.edu/python/2022/psets/6/scourgify/



# Data, too, often needs to be “cleaned,” as by reformatting it, so that values are in a consistent, if not more convenient, format. Consider, for instance, this CSV file of students, before.csv, below:
# Even though each “row” in the file has three values (last name, first name, and house), the first two are combined into one “column” (name), escaped with double quotes, with last name and first name separated by a comma and space. Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge, since it’d be strange to start a letter with:

# Dear Potter, Harry,
# Rather than with, for instance:

# Dear Harry,
# In a file called scourgify.py, implement a program that:

# Expects the user to provide two command-line arguments:
# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

# -------------------------------------------------------------------------------------------------------------------------------------