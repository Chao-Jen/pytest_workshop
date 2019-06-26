import pytest
import numpy as np
from numpy.testing import assert_array_equal

#@pytest.mark.xfail
def test_equality_v1():
    a = np.array([np.nan, 2, 3])
    b = np.array([np.nan, 2, 3])
    # Normally nan compared to anything else, even nan, results in False. 
    # That’s the official, expected behavior. 
    assert (a == b).all()  
    
def test_equality_v2():
    a = np.array([np.nan, 2, 3])
    b = np.array([np.nan, 2, 3])
    # If we want these 2 arrays to be regarded as "equal", 
    # then we may use assert_array_equal.
    assert_array_equal(a, b)
    