class VariableNames(object):
    def __init__(self, names=[]):
        self._names = names

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, values):
        pass

    def __len__(self):
        return len(self._names)
