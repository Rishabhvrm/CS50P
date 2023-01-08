# __init__.py - tells python to treat this folder as a package. Even if it's empty
from hello import hello

def test_hello_default():
    assert hello() == "hello, world"