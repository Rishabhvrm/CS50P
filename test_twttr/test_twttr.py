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