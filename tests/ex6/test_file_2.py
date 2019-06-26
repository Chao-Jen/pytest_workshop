import pytest
import numpy as np
from numpy.testing import assert_allclose

#@pytest.mark.xfail
def test_equality_v1():
    a = np.pi
    b = np.sqrt(np.pi) ** 2
    assert a == b   
    
def test_equality_v2():
    a = np.pi
    b = np.sqrt(np.pi) ** 2
    assert_allclose(a, b)
    
def test_array_equality_v1():
    a = np.array([1.1, np.pi, 3.])
    b = np.array([1.1, np.sqrt(np.pi) ** 2, 4.])
    assert a == b   

#@pytest.mark.xfail
def test_array_equality_v2():
    a = np.array([1.1, np.pi, 3.])
    b = np.array([1.1, np.sqrt(np.pi) ** 2, 4.])
    assert_allclose(a, b)