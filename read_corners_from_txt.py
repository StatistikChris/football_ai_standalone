from ast import literal_eval
import numpy as np
import json

input_file = 'output/coords.txt'

with open(input_file) as file:
    corners = file.read()
    corners = json.dumps(corners)
    corners = json.loads(corners)
    corners = np.array(literal_eval(corners))

print(corners)
