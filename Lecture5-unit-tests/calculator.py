def main():
    x = int(input("Please enter a number and I will square it: "))
    print(square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()