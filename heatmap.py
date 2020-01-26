#import read_player_coords
from read_player_coords import read_coords
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#input_file = 'output/player_coords.txt'
#input_file = 'output/test.txt'
input_file = 'output/mapped_player_coords.txt'

coords = read_coords(input_file)
coords = np.reshape(coords , (-1,3))

coords = pd.DataFrame(coords)
coords.columns = ['frame','x','y']


plt.scatter(x=coords.x , y=coords.y, c=coords.frame)
#plt.xlim(-2, 1500)
#plt.ylim(-2, 750)
#plt.xlim(-2, 3)
#plt.ylim(-2, 3)
cbar = plt.colorbar()
cbar.set_label("frames", labelpad=+1)
plt.show()
