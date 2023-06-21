from fuel import convert
from fuel import gauge

def test_convert_return_correct():
    assert convert("1/2") == 50

def test_convert_return_empty():
    assert convert("1/100") == "E"

def test_convert_return_full():
    assert convert("1/1") == "F"

def test_gauge_return():
    assert gauge(50) == "50%"