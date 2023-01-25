# making this file to demonstrate
# succint way of returning values

def main():
    x = int(input("What's x? "))
    print("Even" if is_even(x) is True else "Odd")
    #if is_even(x):
    #    print("Even")
    #else:
    #    print("odd")

def is_even(x):
    return True if x % 2 == 0 else False

main()