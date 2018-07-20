import json

def read_notebook(path):
    notebook_dct = read_json(path)
    return read_dct(notebook_dct)

def read_dct(dct):
    cells = dct['cells']
    del dct['cells']
    return cells, dct

def read_json(path):
    with open(path) as notebook_file:
        s = notebook_file.read()
        return json.loads(s)