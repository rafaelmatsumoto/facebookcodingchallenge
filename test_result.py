import pytest
from main import ReliefCalculator

@pytest.fixture
def my_calc():
    calculator = ReliefCalculator()
    return calculator

def test_simple(my_calc):
    arr_relief = [2, 1, 2]
    assert my_calc.relief_calc(arr_relief) == 1

def test_zero_relief(my_calc):
    arr_relief = [3, 3, 3, 3]
    assert my_calc.relief_calc(arr_relief) == 0

def test_equality(my_calc):
    arr_relief = [3, 1, 3, 1, 3, 1, 3]
    assert my_calc.relief_calc(arr_relief) == 6

def test_reverse(my_calc):
    arr_relief = [5, 4, 2, 1, 3, 6]
    assert my_calc.relief_calc(arr_relief) == 10

def test_medium(my_calc):
    arr_relief = [6, 3, 2, 1, 5]
    assert my_calc.relief_calc(arr_relief) == 9

def test_zero(my_calc):
    arr_relief = [4, 3, 2, 1]
    assert my_calc.relief_calc(arr_relief) == 0

def test_multiple_columns(my_calc):
    arr_relief = [5, 3, 2, 8, 4, 3, 6]
    assert my_calc.relief_calc(arr_relief) == 10

def test_multiple_columns_2(my_calc):
    arr_relief = [5, 3, 2, 8, 4, 3, 6, 1, 7]
    assert my_calc.relief_calc(arr_relief) == 19

def test_coroutine(my_calc):
    arr_relief = [5, 3, 2, 8, 1, 8, 9, 3, 2, 4]
    assert my_calc.relief_calc(arr_relief) == 15

def test_given_solution(my_calc):
    arr_relief =  [3, 0, 1, 3, 0, 5]
    assert my_calc.relief_calc(arr_relief) == 8