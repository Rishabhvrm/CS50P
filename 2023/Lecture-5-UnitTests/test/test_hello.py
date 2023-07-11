from c_hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("david") == "hello, david"

# Running tests on a package
# have to create a file '__init__.py' so that python can treat this folder/module as a package