# ValueError ~ Runtime Error

# try and except and else
# pass - if you don't want to do anything with catched error

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