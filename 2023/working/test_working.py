from working import convert
import pytest

def test_hours():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_hours_incorrect():
    assert convert("12 AM to 12 PM") != "01:00 to 13:00"

def test_minutes_incorrect():
    assert convert("9:00 AM to 5:00 PM") != "09:05 to 17:00"

# making sure that a ValueError will be raised
# when user omits " to "
def test_format():
    with pytest.raises(ValueError):
        convert("2PM 8AM")

# making sure that a ValueError will be raised
# for incorrect range
def test_range1():
    with pytest.raises(ValueError):
        convert("6:70 AM to 8:90PM")

def test_range2():
    with pytest.raises(ValueError):
        convert("6:00 AM to 8:90PM")

def test_range3():
    with pytest.raises(ValueError):
        convert("34 AM to 8 PM")

