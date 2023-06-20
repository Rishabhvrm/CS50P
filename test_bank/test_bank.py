from bank import value

def test_uppercase():
    assert value("HELLO") == 0

def test_lowercase():
    assert value("hello") == 0

def test_sentence():
    assert value("hello, how are you?") == 20

def test_sentence_wrong():
    assert value('what?') == 100

def test_numbers():
    assert value(123) == 100

def test_whitespace():
    assert value(" ") == 100

def test_punctuation():
    assert value(",.") == 100