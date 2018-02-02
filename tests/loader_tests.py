import dtables
import numpy as np
import pandas as pd
import pytest

from dtables.errors import (ShapeMismatchException,
    MultipleDimentionException,
    LengthMismatchException)

def test_load_dict():
    dt = dtables.load_dict({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    assert dt.variable_names == ['A', 'B']
    assert np.array_equal(dt.data_list[0], [1,2,3])
    assert np.array_equal(dt.data_list[1], [4,5,6])

def test_load_dict_shape_mismatch():
    with pytest.raises(ShapeMismatchException):
        dt = dtables.load_dict({
            'A': [1, 2, 3],
            'B': [4, 5, 6, 7]
        })


def test_load_tuples():
    dt = dtables.load_tuples([('max-temp', 'min-temp'),
        (90, 40),
        (85, 35),
        (95, 40)
        ])
    assert dt.variable_names == ['max-temp', 'min-temp']
    assert np.array_equal(dt.data_list[0], np.array([90,85,95]))
    assert np.array_equal(dt.data_list[1], np.array([40,35,40]))

def test_load_csv():
    dt = dtables.load_csv('./tests/assets/test_csv.csv')

    assert dt.variable_names == ['bool1','category','dates','float64','int64','string','uint8','tdeltas','uint64','other_dates','tz_aware_dates']
    assert np.array_equal(dt.data_list[0], np.array([True, False, True]))
    assert np.array_equal(dt.data_list[1], np.array(['A', 'B', 'C']))
    assert np.array_equal(dt.data_list[2], np.array(['2018-01-01', '2018-01-02', '2018-01-03']))
    assert np.array_equal(dt.data_list[3], np.array([4.0, 5.0,6.0]))
    assert np.array_equal(dt.data_list[5], np.array(['a', 'b', 'c']))
