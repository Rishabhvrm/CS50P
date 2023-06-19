from calculator import square

def main():
    test_square_2()

# convention to name a test function: test_funName()
# def test_square_1():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")



# Notes:
# assert - assert something is true
# instead of using the above code we can use assert
# much simpler and cleaner (no if's)

def test_square_2():
    try:
        assert square(2) == 4           # will raise AssertionError if test failed
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


if __name__ == "__main__":
    main()

# introducing pytest
# unit test - testing individual units of your program