def main():
    greeting = input("Greeting: ")
    print(f'${value(greeting)}')

# all logic performing on greeting should be in this function not in the main
def value(greeting):
    if greeting.lower().strip().startswith("hello"):
        return 0
    elif greeting.lower().strip().startswith("h"):
        return 20
    else: return 100

if __name__ == "__main__":
    main()


# --------------------------------------------------------------------------------------------------------------------------------

# BACK TO THE BANK

# n a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. You can assume that the string passed to the value function will not contain any leading spaces. Only main should call print.

# def main():
#     ...


# def value(greeting):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_bank.py

# --------------------------------------------------------------------------------------------------------------------------------