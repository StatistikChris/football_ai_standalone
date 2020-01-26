from ast import literal_eval
import numpy as np
import json

input_file = 'output/player_coords.txt'

def read_coords(input_file):
    with open(input_file) as file:
        coords = file.read()

    coords = json.dumps(coords)
    coords = json.loads(coords)
    coords = np.array(literal_eval(coords))

    return coords



if __name__=="__main__":
    coords = read_coords(input_file)
    coords = np.reshape(coords , (-1,3))
    print(coords)
