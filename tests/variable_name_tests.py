import dtables
import numpy as np
import pandas as pd
import pytest

from dtables.errors import (ShapeMismatchException,
    MultipleDimentionException,
    LengthMismatchException)

def test_set_variable_names():
    dt = dtables.load_tuples([('max-temp', 'min-temp'),
        (90, 40),
        (85, 35),
        (95, 40)
        ])

    assert dt.variable_names == ['max-temp', 'min-temp']
    dt.variable_names = ['max', 'min']
    assert dt.variable_names == ['max', 'min']

def test_variable_length_mismatch():
    dt = dtables.load_tuples([('max-temp', 'min-temp'),
        (90, 40),
        (85, 35),
        (95, 40)
        ])

    with pytest.raises(LengthMismatchException):
        dt.variable_names = ['max', 'min', 'new']


def test_variable_length_mismatch():
    dt = dtables.load_tuples([('city', 'date', 'max-temp', 'min-temp'),
        ('SFO', '2009-01-01', 90, 40),
        ('SJ', '2009-01-01', 85, 35),
        ('LA', '2009-01-01', 95, 40)
        ])

    dt.variable_names[1] = 'the_date'
    dt.variable_names[2:4] = ['max', 'min']
    dt.variable_names[ [0, 1] ] = ['the_city', 'the_date']
    dt.variable_names['city'] = 'the_city'
    dt.variable_names[ ['city', 'date'] ] = ['the_city', 'the_date']
    dt.variable_names['city':'date'] = ['the_city', 'the_date']
