import count from um


def test_single_um():
    assert count("um") == 1

def test_um_in_word():
    assert count("yummy") == 0

def test_multiple_ums():
    assert count("um um um") == 3

def test_ums_with_other_characters():
    assert count("um, um. (um)") == 3