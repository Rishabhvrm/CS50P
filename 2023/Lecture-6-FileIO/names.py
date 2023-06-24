name = input("What's your name? ")

# part 1, 'open'
# file = open("1names.txt", "w")    # write - it will recreate the file everytime this is called. Hence overwriting new info over old info
file = open("1names.txt", "a")      # append
file.write(f"{name}\n")
file.close()    # close and save the file


# part 2, 'with'
with open("2names.txt", "a") as file:
    file.write(f"{name}\n")

# part 3, read file, rstrip
# with open("1names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello", line.rstrip())

# with open("1names.txt", "r") as file:   # don't need to specify r explicitly, it's default
#     for line in file:
#         print("hello,", line.rstrip())

# -------------------------

# open - like double clicking a file, second argument - what do you want to do this with file (read/write)
# returns a file handle - allows us to access a file
# use 'with' - no need to close explicitly, more pythonic
# rstrip - strip the string