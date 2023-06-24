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

for student in students:
   print(f"{student['name']} is in {student['house']}")




# read csv and sort while reading the file
# declaring a dict - student = {"name": name, "house": house}