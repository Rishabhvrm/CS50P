# introducing pytest
# unit test - testing individual units of your program
# pytest will run all the functions

from calculator import square
import pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# making sure that a TypeError will be raised when something like 'cat' is passed as input
def test_str():
    with pytest.raises(TypeError):
        square("cat")