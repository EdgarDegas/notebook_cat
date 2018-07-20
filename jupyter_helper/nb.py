import json
from . import reader

class Notebook:
    __slots__ = ('cells', 'meta_data')

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = reader.read_notebook(path)

    def json_str(self):
        return json.dumps(self.__json_dct(), indent=4)

    # Override:

    def __getitem__(self, index):
        if self.cells is None:
            raise Exception('No cells in notebook.')
        return self.cells[index]

    def __add__(self, another):
        if self.cells is None or another.cells is None:
            raise Exception('No cells in notebook.')

        result = Notebook()
        result.cells = self.cells + another.cells
        result.meta_data = self.meta_data

        return result


    # Private:
    def __json_dct(self):
        dct = { 'cells': self.cells }
        dct.update(self.meta_data)
        return dct