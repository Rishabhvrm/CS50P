from working import convert


def test_hours():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_hours_incorrect():
    assert convert("12 AM to 12 PM") != "01:00 to 13:00"