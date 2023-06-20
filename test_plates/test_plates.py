from plates import is_valid


def test_starts_with_two_letters():
    assert is_valid("CS50") == True

def test_max_length():
    assert is_valid("ABCDEF") == True

def test_max_length_false():
    assert is_valid("ABCDEFG") == False

def test_min_length():
    assert is_valid("CS") == True

def test_min_length_false():
    assert is_valid("C") == False

def test_num_end():

def test_num_middle():
    assert is_valid("A2AA") == False

def test_punctuation():
    assert is_valid("A.A") == False