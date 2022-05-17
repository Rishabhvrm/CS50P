from hello import hello

def test_hello_default():
    assert hello("david") == "hello, david"
    assert hello() == "hello, world"