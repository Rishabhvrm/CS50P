# ValueError ~ Runtime Error

# try and except and else
# pass - handle the error but pass it

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            #print("Please provide an integer only")
            pass
        else:
            return x
main()