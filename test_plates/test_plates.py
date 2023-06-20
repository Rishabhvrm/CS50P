from plates import is_valid


def test_min_two_chars():
    assert is_valid("CSP50") == True

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