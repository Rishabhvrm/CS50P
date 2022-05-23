name = input("Please enter your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()