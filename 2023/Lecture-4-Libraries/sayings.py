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

# __name__ 's  default value is 'main' when you run a file from command line
# hence it will not be run when it is being imported in another file becuase its defualt value won't be 'main'

# Because it is not being run from the command line, instead it is being called from another file. Hence, the value
# for '__name__' will not be 'main'