import json
from . import reader

class Notebook:
    __slots__ = ('cells', 'meta_data')

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = reader.read_notebook(path)

    def json_str(self):
        return json.dumps(self.__json_dct(), indent=4)


    # Private:
    def __json_dct(self):
        dct = { 'cells': self.cells }
        dct.update(self.meta_data)
        return dct