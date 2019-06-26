import pytest
import numpy as np
import pandas as pd
from pandas.util.testing import assert_frame_equal, assert_series_equal


def test_df_1():
    expected = pd.DataFrame({'a':  [1, np.nan, 3],
                             'b':  [np.nan, 5, 6]},
                             index=['x', 'y', 'z'])
    actual =   pd.DataFrame({'a':  [1, np.nan, 3],
                             'b':  [np.nan, 5, 6]},
                             index=['x', 'y', 'z'])
    assert_frame_equal(actual, expected)

    
#@pytest.mark.xfail
def test_df_2():
    # If two dataframes differ in ordering of columns,
    # by default, assert_frame_equal thorws AssertionError.
    expected = pd.DataFrame({'a':  [1, np.nan, 3],
                             'b':  [np.nan, 5, 6]},
                             index=['x', 'y', 'z'])
    actual =   pd.DataFrame({'b':  [np.nan, 5, 6],
                             'a':  [1, np.nan, 3]},
                             index=['x', 'y', 'z'])
    assert_frame_equal(actual, expected)
    
    
def test_df_3():
    # This test case is almost the same as the above one, 
    # except that check_like=True is passed to assert_frame_equal.
    expected = pd.DataFrame({'a':  [1, np.nan, 3],
                             'b':  [np.nan, 5, 6]},
                             index=['x', 'y', 'z'])
    actual =   pd.DataFrame({'b':  [np.nan, 5, 6],
                             'a':  [1, np.nan, 3]},
                             index=['x', 'y', 'z'])
    assert_frame_equal(actual, expected, check_like=True)

    
#@pytest.mark.xfail
def test_df_4():
    # Let's introduce a difference to column b.
    expected = pd.DataFrame({'a':  [1, np.nan, 3],
                             'b':  [np.nan, 10, 6]},
                             index=['x', 'y', 'z'])
    actual =   pd.DataFrame({'b':  [np.nan, 5, 6],
                             'a':  [1, np.nan, 3]},
                             index=['x', 'y', 'z'])
    assert_frame_equal(actual, expected, check_like=True)