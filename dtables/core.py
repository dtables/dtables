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

    def __repr__( self):
        table_data = []
        variable_names = self.variable_names
        data_list = self.data_list

        table_data.append(variable_names)
        len_data = len(data_list)
        if len_data > 10:
            for index in range(10):
                table_data.append(list(zip(*data_list))[index])
        else:
            for index in range(len(data_list[0])):
                table_data.append(list(zip(*data_list))[index])

        table = AsciiTable(table_data)
        return table.table
