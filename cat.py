import json
import sys

# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []

# read notebook path list
for path in notebook_path_lst:
    notebook = open(path)
    notebook_str = notebook.read()
    notebook_json = json.loads(notebook_str)
    cells = notebook_json['cells']
    cells_lst += cells

target_notebook['cells'] = cells_lst

notebook1 = open(notebook_path1)
notebook1_str = notebook1.read()

notebook1_json = json.loads(notebook1_str)
cells1 = notebook1_json['cells']

notebook2 = open(notebook_path2)
notebook2_str = notebook2.read()
notebook2_json = json.loads(notebook2_str)

cells2 = notebook2_json['cells']

del notebook1_json['cells']


# cat two notebooks
target_cells = cells1 + cells2



# target_notebook['cells'] = target_cells




target_notebook.update(notebook1_json)

target_str = json.dumps(target_notebook)



target = open('target_notebook.ipynb', 'w')
target.write(target_str)