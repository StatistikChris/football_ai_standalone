from ast import literal_eval
import numpy as np
import json
import cv2

def read_corners(input_file):
    with open(input_file) as file:
        corners = file.read()
        corners = json.dumps(corners)
        corners = json.loads(corners)
        corners = np.array(literal_eval(corners))

    return corners


def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")

	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]

	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
    # original order: 0,2,1,3


	# return the ordered coordinates
	return rect


class transform:
    def __init__(self, corners):
        self.corners = corners

    def coord_transform(self, point):
        tl, tr, br, bl = self.corners[0], self.corners[1], self.corners[2], self.corners[3]
        rect = order_points(self.corners)

        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))

        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))

        dst = np.array([[0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype = "float32")


        #dst = np.array([
        #    [0, maxHeight - 1],
        #    [maxWidth - 1, maxHeight - 1],
        #    [0, 0],
        #    [maxWidth - 1, 0],
        #    ], dtype = "float32")


        #dst = np.array([[0, 0],
        #    [0.5, 0],
        #    [0.5, 0.5],
        #    [0, 0.5]] , dtype = "float32")

        #M = cv2.getPerspectiveTransform(rect, dst)
        M, status = cv2.findHomography(rect, dst)

        point.append(1)
        warped = M.dot(point)
        #point = np.array(point, dtype=float32)
        #pts1 = point.reshape(-1,1,2).astype(np.float32)
        #warped = cv2.perspectiveTransform(pts1, M)
        #warped = [warped[0],warped[1]]

        return warped[0:2]
        #return warped
