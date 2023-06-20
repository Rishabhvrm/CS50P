from bank import value

def test_lowercase():
    assert value("hello") == 0

def test_sentence():
    assert value("hey, how are you?") == 20

def test_sentence_wrong():
    assert value('what?') == 100

def test_numbers():
    assert value('123') == 100

def test_whitespace():
    assert value(" ") == 100

def test_punctuation():
    assert value(",.") == 100

def test_case_insensitive():
    assert value("Hello, HOW ARE YOU") == 0