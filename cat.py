import sys
from jupyter_helper import nb

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')

# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook_dct = {}

# read notebooks
target_notebook = nb.Notebook(notebook_path_lst[0])

for path in notebook_path_lst[1:]:
    target_notebook += nb.Notebook(path)

with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_notebook.json_str())