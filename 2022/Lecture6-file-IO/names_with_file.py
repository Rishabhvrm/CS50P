# open and with

name = input("Please enter your name? ")

#file = open("names.txt", "a")

# write in the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# no need for closing now bcz we're using 'with'
# file.close()

# reading lines and returning as a list
# file.readlines()

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

# doing the above thing in a different way
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

# if I want to sort the data that I'm reading
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"helllloooo, {name}")