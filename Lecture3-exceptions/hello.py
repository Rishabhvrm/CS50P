# ValueError ~ Runtime Error

# try and except and else

while true:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("Please provide an integer only")
    else:
        print(f"x is {x}")