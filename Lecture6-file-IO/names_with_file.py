name = input("Please enter your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()