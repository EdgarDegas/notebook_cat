import json
from . import reader

class Notebook:
    """Read path, extract cells and meta_data from file.
    """

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = reader.read_file(path)

    def __add__(self, another):
        cells = self.cells + another.cells
        notebook = Notebook()
        notebook.cells = cells
        notebook.meta_data = self.meta_data

        return notebook

    def jsons(self):
        dct = {'cells':self.cells}
        dct.update(self.meta_data)
        return json.dumps(dct, indent=4)