import numpy as np
from .core import DTable

def load_dict(d):
    column_names = []
    data_list = []
    for k in sorted( d.keys()):
        data_list.append( np.array( d[k]))
        column_names.append( k)

    dt = DTable(column_names=column_names, data_list=data_list)
    return dt
