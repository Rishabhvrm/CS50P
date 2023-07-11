from fuel import convert
from fuel import gauge
import pytest

def test_convert_return_correct():
    assert convert("1/2") == 50

def test_convert_return_empty():
    assert convert("1/100") == 1

def test_convert_return_empty2():
    assert convert("1/99") == 1

def test_convert_return_full():
    assert convert("1/1") == 100

def test_gauge_return():
    assert gauge(50) == "50%"

def test_gauge_return_empty1():
    assert gauge(1) == "E"

def test_gauge_return_empty2():
    assert gauge(0) == "E"

def test_gauge_return_full1():
    assert gauge(99) == "F"

def test_gauge_return_full2():
    assert gauge(100) == "F"

# making sure that a ValueError will be raised
# when a string is passed instead of an integer
def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("cat/dog")

# making sure that a ValueError will be raised
# when x > y
def test_convert_invalid_input2():
    with pytest.raises(ValueError):
        convert("2/1")

# making sure that a ZeroDivisonError will be raised
# when y = 0 is passed
def test_convert_invalid_y():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")