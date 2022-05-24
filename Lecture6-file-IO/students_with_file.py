with open("students_hogwarts.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        # assigning 2 variables at once
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")