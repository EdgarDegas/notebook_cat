import sys
from JupyterHelper import nb

# read argument
argv = sys.argv[1:]
if len(argv) < 2: raise Exception('参数数量必须 >= 2')

# read notebooks from paths (aka(即) argv)
notebook_lst = []

for path in argv:
    if '.ipynb' not in path:
        path += '.ipynb'
    notebook_lst.append(nb.Notebook(path))

target_notebook = notebook_lst[0]
for notebook in notebook_lst[1:]:
    target_notebook += notebook

with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_notebook.jsons())