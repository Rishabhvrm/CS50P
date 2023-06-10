def main():
    hello('world')
    goodbye('people')

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye, {name}')


# Instead of calling 'main' like this
# main()

# use this
if __name__ == "__main__":
    main()
