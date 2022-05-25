import csv

students = []

with open("students_home.csv") as file:
    # stores values as a list of colum
    '''
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})
    '''
    # using DictReader, not a list of columns but a dictionary of columns
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name"}: row["name"], {"home"}: row["home"])

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")