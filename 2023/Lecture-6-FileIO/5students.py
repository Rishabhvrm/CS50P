# using csv dictionary reader

import csv

students = []

with open("5students.csv") as file:
    reader = csv.DictReader(file)   # load dictionary of columns, returns dictionary
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")