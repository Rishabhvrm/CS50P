# write a csv



import csv

name = input("Name: ")
home = input("Home: ")

# Part A - using writer
# with open("6students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])   # write a list of name and home

# Part B - using DictWriter
with open("6students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])  # order of colu mns
    writer.writerow({"name": name, "home": home}) # provide a dictionary