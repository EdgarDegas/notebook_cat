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
for path in notebook_path_lst:
    notebook_lst.append(Notebook(path))

# read cells from notebooks
cells_lst = []
for notebook in notebook_lst:
    cells_lst += notebook.cells

# write target notebook
target_notebook = Notebook()
target_notebook.cells = cells_lst
target_notebook.meta_data = notebook_lst[0].meta_data

with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_notebook.json_str())