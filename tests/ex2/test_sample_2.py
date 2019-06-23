import my_app

def test_case_1():
    lst_input = "Ironman"
    expected = "Iro"
    
    assert my_app.grab_first_three(lst_input) == expected
    
def test_case_2():
    lst_input = "ab"
    expected = "ab"
    
    assert my_app.grab_first_three(lst_input) == expected