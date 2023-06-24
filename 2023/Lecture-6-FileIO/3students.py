students = []

# read csv and sort while reading the file
with open("3students.csv") as file:
   for line in file:
      name, house = line.rstrip().split(",")
      student = {}
      student['name'] = name
      student['house'] = house
      students.append(student)

print(students)




# read csv and sort while reading the file