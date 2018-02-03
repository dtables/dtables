import dtables
import numpy as np
import pandas as pd
import pytest
from terminaltables import AsciiTable
from dtables.errors import (ShapeMismatchException,
    MultipleDimentionException,
    LengthMismatchException)

def test_view():
    dt = dtables.load_dict({
        'A': [5,3,8,6,5,9,12,4,6,8,0,1],
        'B': [6,9,0,7,5,3,2,7,1,90,3,2]
    })

    assert dt.view() == '''+---+---+
| A | B |
+---+---+
| 5 | 6 |
| 3 | 9 |
| 8 | 0 |
| 6 | 7 |
| 5 | 5 |
+---+---+'''


def test_view_start_index():
    dt = dtables.load_dict({
        'A': [5,3,8,6,5,9,12,4,6,8,0,1],
        'B': [6,9,0,7,5,3,2,7,1,90,3,2]
    })
    assert dt.view(5, 5) == '''+----+----+
| A  | B  |
+----+----+
| 9  | 3  |
| 12 | 2  |
| 4  | 7  |
| 6  | 1  |
| 8  | 90 |
+----+----+'''


def test_repr_out_of_bounds():
    dt = dtables.load_dict({
        'A': [5,3,8,6,5,9,12,4,6,8,0,1],
        'B': [6,9,0,7,5,3,2,7,1,90,3,2]
    })

    with pytest.raises(IndexError):
        dt.view(15, 4)


def test_view_fewer_rows():
    dt = dtables.load_dict({
        'A': [5,3],
        'B': [6,9]
    })
    assert dt.view() == '''+---+---+
| A | B |
+---+---+
| 5 | 6 |
| 3 | 9 |
+---+---+'''
