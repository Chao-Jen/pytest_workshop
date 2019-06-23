import pytest
from my_calculator import division

@pytest.mark.parametrize("a", [1, 2, 3, 4])
def test_division_param(a):
    assert division(a, 1) == a
    
@pytest.mark.parametrize("a,b,expected", [(4,2,2), (9,3,3)])
def test_division_param_2(a, b, expected):
    assert division(a, b) == expected