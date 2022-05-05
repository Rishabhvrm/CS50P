# ValueError ~ Runtime Error

# try and except

try:
    x = int(input("What's x? "))

except ValueError:
    print("Please provide an integer only")

print(f"x is {x}")