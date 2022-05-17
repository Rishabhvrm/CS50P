from hello import hello

def test_hello_default():
    assert hello() == "hello, world"

def test_hello_argument():
    assert hello("david") == "hello, david"

def test_hello_argument_using_loop():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"