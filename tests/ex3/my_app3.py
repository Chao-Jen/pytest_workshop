def grab_first_three(lst):
    if len(lst) < 3:
        raise ValueError("The length of lst is less than 3.")
        
    return lst[:3]