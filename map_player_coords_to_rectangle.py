import read_player_coords
from read_player_coords import read_coords
import transform_source
from transform_source import read_corners, transform, order_points
import numpy as np


# get coords of detected players
player_coords_file = 'output/player_coords.txt'
#player_coords_file = 'output/test.txt'
coords = read_coords(player_coords_file)
coords = np.reshape(coords , (-1,3))

# get coords of the four corners
corners_file = 'output/coords.txt'
corners = read_corners(corners_file)
corners = order_points(corners)
mapping = transform(corners)

output_file = 'output/mapped_player_coords.txt'

# old coords have to be mapped to new coords element by element
new_coords = []

for c in coords:
    f, x ,y = c # frame, x-coord, y-coord
    point = [x,y] # mapping functions expects 2dim input

    new_point = mapping.coord_transform(point)
    new_coords.append(f) # append elements to list of new_coords
    new_coords.append(new_point[0])
    new_coords.append(new_point[1])
    #new_coords.append(new_point[2])
    #new_coords.append(new_point[3])

if __name__=="__main__":
    print(new_coords)
    with open(output_file,'w+') as file:
        file.write(str(new_coords))
