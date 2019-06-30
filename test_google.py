from remaining_integer import RemainingInteger

def test_simple():
    rem = RemainingInteger()
    arr = [6, 1, 3, 3, 3, 6, 6]
    assert rem.find_remaining_integer(arr) == 1