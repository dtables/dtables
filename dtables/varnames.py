class VariableNames(object):
    def __init__(self, names=[]):
        self._names = names

    def __getitem__(self, index_or_slice ):
        return self._names[index_or_slice]

    #def __setitem__(self, index, values):
        #self._names[index] = values

    def __iter__( self):
        for name in self._names:
            yield name


    def __len__(self):
        return len(self._names)
