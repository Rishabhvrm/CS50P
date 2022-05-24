import csv

students = []

with open("students_home.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for name, home in students:
    print(f"{name} is from {home}")