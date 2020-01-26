import transform_source
from transform_source import read_corners, order_points, transform

# specify file for coordinates of the four corners
input_file = 'output/coords.txt'

# read the corners from file
corners = read_corners(input_file)

# create mapping matrix out of corners
mapping_matrix = transform(corners)

# specify a point
# [[114, 108], [431, 146], [288, 425], [134, 469]]
point = [114,108] # 0,0
# point = [431, 146] # 160, 0
# point = [288, 425] # 80, 90
# point = [134, 469] # 0,110

# Start of the main program here
if __name__=="__main__":
    # map point to rectangular
    new_point = mapping_matrix.coord_transform(point)

    print(new_point)
