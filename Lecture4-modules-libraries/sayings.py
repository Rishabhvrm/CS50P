def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

main()

# __name__ is a built-in variable which evaluates to the name of the current module
#print("File __name__ is = %s" % __name__)