import json

class Notebook:
    __slots__ = ('cells', 'meta_data')

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = self.read_notebook(path)

    def read_notebook(self, path):
        notebook_dct = self.read_json(path)
        return self.read_dct(notebook_dct)

    def read_dct(self, dct):
        cells = dct['cells']
        del dct['cells']
        return cells, dct

    def read_json(self, path):
        with open(path) as notebook_file:
            s = notebook_file.read()
            return json.loads(s)

    def json_str(self):
        return json.dumps(self.json_dct(), indent=4)


    def json_dct(self):
        dct = { 'cells': self.cells }
        dct.update(self.meta_data)
        return dct