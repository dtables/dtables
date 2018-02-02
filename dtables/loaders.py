import numpy as np
import pandas as pd
from .core import DTable
from .errors import (ShapeMismatchException,
    MultipleDimentionException)

def load_dict(d):
    variable_names = []
    data_list = []
    expected_value_count = None

    for k in sorted( d.keys()):
        values = d[k]
        if expected_value_count is None:
            expected_value_count = len(values)
        elif expected_value_count != len(values):
            raise ShapeMismatchException("Column {} has {} values. Expected it to have {} values.".format(k, len(values), expected_value_count))

        data_list.append( np.array( values))
        variable_names.append( k)

    dt = DTable(variable_names=variable_names, data_list=data_list)
    return dt


def load_tuples(t, header = True):
    variable_names = []
    data_list = []

    len_list = [len(e) for e in t]
    if( len( set( len_list)) != 1):
        for index in range(len(len_list)-1):
            if len_list[index] != len_list[index + 1]:
                raise ShapeMismatchException("Data expected to have {} columns, value at index {} indicates {} columns".format(len_list[0], index + 1, len_list[index + 1]))

    if header == True:
        variable_names = list(t[0])
        data_list = [np.array(l) for l in zip(*t[1:])]
    else:
        data_list = [np.array(l) for l in zip(*t)]

    dt = DTable(variable_names=variable_names, data_list=data_list)
    return dt

def load_csv(*args, **kwargs):
    variable_names = []
    data_list = []

    df = pd.read_csv(*args, **kwargs)
    variable_names = list(df.columns)
    for col in df.columns:
        data_list.append(df[col].values)

    dt = DTable(variable_names=variable_names, data_list=data_list)
    return dt
