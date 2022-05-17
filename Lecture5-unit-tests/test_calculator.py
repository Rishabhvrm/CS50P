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
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()