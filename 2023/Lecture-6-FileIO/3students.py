students = []

# read csv and sort while reading the file
with open("3students.csv") as file:
   for line in file:
      name, house = line.rstrip().split(",")
      student = {}                      # use this for line 7, 8, 9 -> student = {"name": name, "house": house}
      student["name"] = name
      student["house"] = house
      students.append(student)

# def get_name(student):
#    return student['name']

# refer code in next section to use lambda function to call get_name()
# for student in sorted(students, key=get_name, reverse=True):
#    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# read csv and sort while reading the file
# declaring a dict - student = {"name": name, "house": house}
# functions as arguments into other functions
# sorting a list of dictionaries
# lambda function