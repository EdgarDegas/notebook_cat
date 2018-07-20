import json

class Notebook:
    def __init__(self, path):
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