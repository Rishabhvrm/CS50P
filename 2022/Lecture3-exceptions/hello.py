# ValueError ~ Runtime Error

# try and except and else
# pass - if you don't want to do anything with catched error

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt_msg):
    while True:
        try:
            x = int(input(prompt_msg))
        except ValueError:
            #print("Please provide an integer only")
            pass
        else:
            return x
main()