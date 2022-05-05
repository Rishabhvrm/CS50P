# ValueError ~ Runtime Error

# try and except

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("Please provide an integer only")