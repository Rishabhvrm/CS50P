students = []

with open("3students.csv") as file:
   for line in file:
      name, house = line.rstrip().split(",")
      students.append(f"{name} is in {house}")