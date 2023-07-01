from numb3rs import validate

def test_five_digit_ip():
    assert validate('1.2.3.4.5') == False

def test_out_of_range():
    assert validate('300.1.2.3') == False

def test_in_range():
    assert validate('1.2.3.4') == True