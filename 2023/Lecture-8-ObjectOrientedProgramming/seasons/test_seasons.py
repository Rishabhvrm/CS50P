from seasons import calculate_minutes

def test_past_year():
    assert("2022-08-20") == "Five hundred twenty-five thousand, six hundred minutes"

def test_today():
    assert("2023-08-20") == "Zero minutes"

def test_future_year():
    assert("2024-08-20") == "Minus five hundred twenty-seven thousand forty minutes"

def test_invalid_date():
    assert("2022/08/20") == "Invalid date"

def test_ordinal_date():
    assert("August 20, 2022") == "Invalid date"