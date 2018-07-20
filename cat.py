import json
import sys

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')


# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []

# read notebook path list
for path in notebook_path_lst:
    with open(path) as notebook:
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)

        # read cells
        cells = notebook_json['cells']

        # take meta data from first notebook
        if path is notebook_path_lst[0]:
            del notebook_json['cells']
            meta_data = notebook_json

        # add cells into cells_lst
        cells_lst += cells

target_notebook['cells'] = cells_lst
target_notebook.update(meta_data)

target_str = json.dumps(target_notebook)

with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_str)