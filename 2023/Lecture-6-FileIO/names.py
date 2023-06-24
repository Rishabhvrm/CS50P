name = input("What's your name? ")

# file = open("1names.txt", "w")    # write - it will recreate the file everytime this is called. Hence overwriting new info over old info
file = open("1names.txt", "a")      # append
file.write(name)
file.close()    # close and save the file

# -------------------------

# open - like double clicking a file, second argument - what do you want to do this with file (read/write)
# returns a file handle - allows us to access a file