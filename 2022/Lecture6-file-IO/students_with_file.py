with open("students_hogwarts.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        # assigning 2 variables at once
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

print("HOLD UP!!!")

# if I want to sort it
students = []

with open("students_hogwarts.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["house"] = house
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")


# functions as arguments

print("HOLD UP AGAIN!!!")

def get_name(stud):
    return stud["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")


# using lambda function instead of a separate function
print("HOLD UP AGAIN!!!")

for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}")
