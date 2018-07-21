import json
import sys


# read argument
argv = sys.argv[1:]
if len(argv) < 2: raise Exception('参数数量必须 >= 2')



# read notebooks from paths (aka(即) argv)
target_cells = []

for path in argv:
    with open(path) as notebook_file:
        s = notebook_file.read()
        notebook_dct = json.loads(s)
        target_cells += notebook_dct['cells']


        if path is argv[0]:
            del notebook_dct['cells']
            meta_data = notebook_dct

target_notebook = {
    'cells': target_cells
}

target_notebook.update(meta_data)
target_str = json.dumps(target_notebook, indent=4)

with open('target_notebook.ipynb', 'w') as target_file:
    target_file.write(target_str)