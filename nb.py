import json

class Notebook:
    """Read path, extract cells and meta_data from file.
    """

    def __init__(self, path=None):
        if path is not None:
            self.cells, self.meta_data = self.__read_file(path)

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

    def __read_file(self, path):
        # return cells, meta_data
        with open(path) as notebook_file:
            s = notebook_file.read()
            return self.__read_jsons(s)

    def __read_jsons(self, jsons):
        """Read json str.
        Return cells (list) and meta_data(dict).
        """
        notebook_dct = json.loads(jsons)
        cells = notebook_dct['cells']
        del notebook_dct['cells']

        return cells, notebook_dct
