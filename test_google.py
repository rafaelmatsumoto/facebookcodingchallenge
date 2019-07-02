from remaining_integer import RemainingInteger

def test_simple():
    rem = RemainingInteger()
    arr = [6, 1, 3, 3, 3, 6, 6]
    assert rem.find_remaining_integer(arr) == 1

def test_middle_number():
    rem = RemainingInteger()
    arr = [1, 2, 3, 1, 3, 1, 3]
    assert rem.find_remaining_integer(arr) == 2

def test_last_number():
    rem = RemainingInteger()
    arr = [50, 60, 4, 2, 4, 4, 2, 13, 50, 2, 13, 50, 13]
    assert rem.find_remaining_integer(arr) == 60