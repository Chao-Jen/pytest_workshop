import my_app3
from pytest import raises

def test_case_short_input():
    lst_input = "pi"
    
    with raises(ValueError):
        my_app3.grab_first_three(lst_input)