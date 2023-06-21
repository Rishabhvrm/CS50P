from fuel import convert
from fuel import gauge

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

def test_convert_value_error():
    assertRaises convert("cat/dog") raise ValueError

def test_gauge_return_full2():
    assert gauge(100) == "F"