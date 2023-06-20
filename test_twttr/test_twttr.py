from twttr import shorten

def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_lowercase():
    assert shorten('oblivion') == 'blvn'

def test_space():
    assert shorten(' ') == ' '

def test_nil():
    assert shorten('') == ''

def test_string():
    assert shorten('this string has vowels') == 'ths strng hs vwls'

def test_number():
    assert shorten('123a45') == '12345'

def test_punctuation():
    assert shorten('Bond, James)