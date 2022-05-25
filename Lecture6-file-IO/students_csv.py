import csv

students = []

with open("students_home.csv") as file:
    #reader = csv.reader(file), stores values as a list of colum
    # using DictReader, not a list of columns but a dictionary of columns

    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")