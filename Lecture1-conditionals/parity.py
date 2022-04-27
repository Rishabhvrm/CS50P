def main():
    n = int(input("What's x? "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()