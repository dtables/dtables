from terminaltables import AsciiTable

class DTable(object):
    def __init__(self, variable_names=[], data_list=[]):
        self.variable_names = variable_names
        self.data_list = data_list

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
