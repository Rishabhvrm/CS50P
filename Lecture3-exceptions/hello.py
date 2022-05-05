# ValueError ~ Runtime Error

# try and except and else

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("Please provide an integer only")
        else:
            break
    return x
main()