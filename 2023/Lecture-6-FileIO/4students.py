import csv

students = []

with open("3students.csv") as file:
    reader = csv.reader(file)   # returns list
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

# use CSV library
# handling the problem if a value already has a comma in it