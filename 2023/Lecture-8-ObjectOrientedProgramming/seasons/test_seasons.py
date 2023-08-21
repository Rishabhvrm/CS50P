from seasons import calculate_minutes
import pytest

def test_past_year():
    assert calculate_minutes("2022-08-20") == "Five hundred twenty-five thousand, six hundred minutes"

def test_today():
    assert calculate_minutes("2023-08-20") == "Zero minutes"

def test_future_year():
    assert calculate_minutes("2024-08-20") == "Minus five hundred twenty-seven thousand forty minutes"

# making sure that a ValueError will be raised
# for incorrect date format
def test_ordinal_date():
    with pytest.raises(ValueError):
        calculate_minutes("August 20, 2022")

def test_incorrect_format_date():
    with pytest.raises(ValueError):
        calculate_minutes("2022/08/20")
