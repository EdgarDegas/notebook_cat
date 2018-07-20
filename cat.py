import json
import sys

from notebook import Notebook

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')

# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook_dct = {}

# read notebooks
notebook_lst = []

# read notebook path list
for path in notebook_path_lst:
    notebook_lst.append(Notebook(path))

# read cells from notebooks
cells_lst = []
for notebook in notebook_lst:
    cells_lst.append(notebook.cells)

# read meta data from a random notebook in notebook_lst
target_notebook_dct['cells'] = cells_lst
target_notebook_dct.update(notebook_lst[0].meta_data)


# convert to json string and export to target_notebook.ipynb
target_str = json.dumps(target_notebook_dct)
with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_str)