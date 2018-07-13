import json
import sys

# accept argument
notebook_path1 = sys.argv[1] 
notebook_path2 = sys.argv[2]



# read notebooks
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

target_notebook = {}

target_notebook['cells'] = target_cells
target_notebook.update(notebook1_json)

target_str = json.dumps(target_notebook)



target = open('target_notebook.ipynb', 'w')
target.write(target_str)