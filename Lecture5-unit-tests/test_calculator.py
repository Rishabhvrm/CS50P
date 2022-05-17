# writing tests on our own

from calculator import square

def main():
    test_square()

# without assert
'''
def test_square():
    if square(2) != 4:
        print("2 squared was not 4, test case failed")
    if square(3) != 9:
        print("3 squared was not 9, test case failed")
'''

# using assert
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4, test case failed")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9, test case failed")

if __name__ == "__main__":
    main()