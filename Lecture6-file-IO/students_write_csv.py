import csv

name = input("What's your name? ")
home = input("Where do you come from? ")

with open("characters.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home}) # takes input as a dictionary