from plates import is_valid


def test_min_two_chars():
    assert is_valid("CS50") == True

def test_string():
    assert is_valid("hello, world") == False

def test_max_length():
    assert is_valid("ABCDEF") == True

def test_max_length_false():
    assert is_valid("ABCDEFG") == False

def test_min_length():
    assert is_valid("CS") == True

def test_min_length_false():
    assert is_valid("C") == False

def test_num_end():
    assert is_valid("AAA222") == True

def test_num_middle():
    assert is_valid("CS50P") == False

def test_punctuation():
    assert is_valid("A.A") == False

def test_starts_with_number():
    assert is_valid("50CS") == False

def test_all_num():
    assert is_valid("1234") == False

def test_first_num_zero():
    assert is_valid("CS05") == False

def test_numeric():
    assert is_valid("50") == False

def test_aplha_numeric():
    assert is_valid("PI3.14") == False


# -------------------------------------------------------------------------------------------------------------------
# Re-requesting a Vanity Plate

# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()
# Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

# pytest test_plates.py

# -------------------------------------------------------------------------------------------------------------------