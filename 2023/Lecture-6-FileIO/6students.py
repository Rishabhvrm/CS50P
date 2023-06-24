# write a csv

import csv

name = input("Name: ")
home = input("Home: ")

with open("6students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])   # write a list of name and home
    