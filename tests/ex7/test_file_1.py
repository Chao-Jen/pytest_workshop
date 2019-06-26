import pytest
import pandas as pd
from pandas.util.testing import assert_frame_equal, assert_series_equal

#@pytest.mark.xfail
def test_series_1():
    s1 = pd.Series([1, 2, 3], dtype='int')
    s2 = pd.Series([1, 2, 3], dtype='float')
    # Using simple assert is not the right way to compare two series.
    assert s1 == s2
    
#@pytest.mark.xfail    
def test_series_2():
    s1 = pd.Series([1, 2, 3], dtype='int')
    s2 = pd.Series([1, 2, 3], dtype='float')
    # assert_series_equal produces more informative output.
    assert_series_equal(s1, s2)
    
def test_series_3():
    s1 = pd.Series([1, 2, 3], dtype='int')
    s2 = pd.Series([1, 2, 3], dtype='float')
    # assert_series_equal allows different level of strictness of equality.
    assert_series_equal(s1, s2, check_dtype=False)