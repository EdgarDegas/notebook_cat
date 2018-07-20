import json

class Notebook:
    __slots__ = ('cells', 'meta_data')

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = self.__read_notebook(path)

    def json_str(self):
        return json.dumps(self.__json_dct(), indent=4)


    # Private:
    def __read_notebook(self, path):
        notebook_dct = self.__read_json(path)
        return self.__read_dct(notebook_dct)

    def __read_dct(self, dct):
        cells = dct['cells']
        del dct['cells']
        return cells, dct

    def __read_json(self, path):
        with open(path) as notebook_file:
            s = notebook_file.read()
            return json.loads(s)

    def __json_dct(self):
        dct = { 'cells': self.cells }
        dct.update(self.meta_data)
        return dct