# making this file to take notes from Lecture-3-Exceptions

# Errors
# try and except
# else
# pass

## 'SyntaxError'
## 'ValueError'
# will throw a 'ValueError' if anything other than int is given in the input
#x = int(input("What's x: "))
#print(x)

# use try and except
try:
    x = int(input("What's x: "))
    print(f"x is {x}")
except ValueError:
    print('x is not an integer')

# try to put only one line/few lines of code
# under try that can actually raise an error
# like in above code, print is not gonna raise any error
# so it's better to put only input line under try

# below code does what above comment says
# but it introduces 'NameError' if user doesn't give int
# bcz x is never defined
try:
    x = int(input("What's x: "))
except ValueError:
    print('x is not an integer')
print(f"x is {x}")

# to tackle above
# use 'else'
# i.e. if nothing goes wrong, do the 'else' part
# it will get executed only if try is succeeded

while True:
    try:
        x = int(input("What's x: "))
    except ValueError:
        print('x is not an integer')
    else:
        break

print(f"x is {x}")

# use of 'pass'
# 'pass' just simply do nothing,
# it's like your in a group and now it's your turn to speak up,
# you just say 'pass'

while True:
    try:
        x = int(input("What's x: "))
        break
    except ValueError:
        pass

print(f"x is {x}")


# more pythonic way is to 'try' something
# except if it doesn't work
# # also 'raise' - we can raise exceptions

def main():
    x = get_int("What's x? ")
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()