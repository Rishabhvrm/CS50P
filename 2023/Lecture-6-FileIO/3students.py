students = []

# read csv and sort while reading the file
with open("3students.csv") as file:
   for line in file:
      name, house = line.rstrip().split(",")
      student = {}                      # use this for line 7, 8, 9 -> student = {"name": name, "house": house}
      student["name"] = name
      student["house"] = house
      students.append(student)

print(students)

def get_name(student):
   return student['name']

for student in sorted(students, key=get_name, reverse=True):
   print(f"{student['name']} is in {student['house']}")


# read csv and sort while reading the file
# declaring a dict - student = {"name": name, "house": house}
# functions as arguments into other functions
# sorting a list of dictionaries