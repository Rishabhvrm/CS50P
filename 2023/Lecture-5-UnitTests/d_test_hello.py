from c_hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("david") == "hello, david"

def test_argument_2():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f'hello, {name}'