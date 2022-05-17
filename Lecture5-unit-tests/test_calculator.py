from calculator import square

def test_square():
    if square(2) != 4:
        print("2 squared was not 4, test case failed")