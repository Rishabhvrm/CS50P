from fuel import convert
from fuel import gauge

def test_convert_return():
    assert convert("1/2") == 50

def test_gauge_return():
    assert gauge(50) == "50%"