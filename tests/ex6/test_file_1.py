import pytest
import pytest
import numpy as np
from numpy.testing import assert_array_equal

#@pytest.mark.xfail
def test_equality_v1():
    a = np.array([0., 1., 2., 3.])
    b = np.array([0., 1., 2., 3.])
    assert a == b        
    
def test_equality_v2():
    a = np.array([0., 1., 2., 3.])
    b = np.array([0., 1., 2., 3.])
    assert_array_equal(a, b)
    
def test_difference_v1():
    a = np.array([0., 1., 2., 3.])
    b = np.array([0., 1., 2., 3., 4.])
    assert a == b
    
def test_difference_v2():
    a = np.array([0., 1., 2., 3.])
    b = np.array([0., 1., 2., 3., 4.])
    assert_array_equal(a, b)
    
