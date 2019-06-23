import my_app

def test_case_1():
    lst_input = "Koh Lih Pin"
    expected = "Koh"
    
    assert my_app.grab_first_three(lst_input) == expected
    