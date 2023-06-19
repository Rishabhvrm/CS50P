from c_hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("david") == "hello, david"