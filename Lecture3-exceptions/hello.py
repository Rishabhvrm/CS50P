# ValueError ~ Runtime Error

# try and except and else

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("Please provide an integer only")
    else:
        break

print(f"x is {x}")
        