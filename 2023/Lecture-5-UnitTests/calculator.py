def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2

# do this proactively to make sure that main is only called when this particular file
# is being run through cmd.
# Not when some other file is importing this file and calling this function
if __name__ == "__main__":
    main()