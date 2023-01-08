# Using Functions


def main():
    name = input("What's your name? ")
    hello(name)

# passing default value to the input parameter
def hello(to="world!"):
    print("hello,", to)

main()