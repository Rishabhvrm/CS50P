# ValueError ~ Runtime Error

# try and except and else

try:
    x = int(input("What's x? "))

except ValueError:
    print("Please provide an integer only")

else:
    print(f"x is {x}")