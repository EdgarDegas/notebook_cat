import json

def read_file(path):
    # return cells, meta_data
    with open(path) as notebook_file:
        s = notebook_file.read()
        return read_jsons(s)

def read_jsons(jsons):
    """Read json str.
    Return cells (list) and meta_data(dict).
    """
    notebook_dct = json.loads(jsons)
    cells = notebook_dct['cells']
    del notebook_dct['cells']

    return cells, notebook_dct
