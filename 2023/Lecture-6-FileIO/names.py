name = input("What's your name? ")

file = open("1names.txt", "w")
file.write(name)
file.close()    # close and save the file

# -------------------------

# open - like double clicking a file, second argument - what do you want to do this with file (read/write)
# returns a file handle - allows us to access a file