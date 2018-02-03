from terminaltables import AsciiTable
from .errors import LengthMismatchException
from .varnames import VariableNames

class DTable(object):
    def __init__(self, variable_names=[], data_list=[]):
        self.data_list = data_list
        self.variable_names = variable_names

    @property
    def variable_names(self):
        return self._variable_names

    @variable_names.setter
    def variable_names( self, new_variable_names):
        if len(new_variable_names) != len(self.data_list):
            raise LengthMismatchException('{} variables passed, expecected {}'.format(
                len(new_variable_names), len(self.data_list)))
        self._variable_names = VariableNames(new_variable_names)

    def view( self, start_index = 0, count = 5):
        table_data = []
        variable_names = self.variable_names
        data_list = self.data_list
        len_data = len(data_list[0])
        if len_data < start_index+count: count = len_data - start_index
        table_data.append(variable_names)

        if len_data < start_index:
            raise IndexError('{} is greater than the length of the data'.format(start_index))

        for index in range(start_index, start_index+count, 1):
            table_data.append(list(zip(*data_list))[index])

        table = AsciiTable(table_data)
        return table.table

    def head( self, n = None):
        if not n: n = 5
        return self.view(0, n)

    def tail( self, n = None):
        data_list = self.data_list
        len_data = len(data_list[0])

        if not n: n = 5
        return self.view(len_data - n, n)

    def __repr__( self):
        data_list = self.data_list
        len_data = len(data_list[0])
        if len_data > 10:
            return self.view(0, 10)
        else:
            return self.view(0, len_data)
