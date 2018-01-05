import dtables
import numpy as np

def test_load_dict():
    dt = dtables.load_dict({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })

    assert dt.column_names == ['A', 'B']
    assert np.array_equal(dt.data_list[0], [1,2,3])
    assert np.array_equal(dt.data_list[1], [4,5,6])
