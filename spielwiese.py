import numpy as np
import cv2

point = [0,1]
point.append(3)

#print(point)


pts = np.array([[1,2,],[3,4]], np.float32)

M = np.array([[ 3.9643041e-04,  6.5913662e-07,  3.1965813e-03],
              [ 7.4297395e-07, -3.9652368e-04, -4.4492882e-04],
              [-9.3076696e-06, -3.5773560e-06,  1.0000000e+00]], dtype=np.float32)

## (n, 1, 2)
pts1 = pts.reshape(-1,1,2).astype(np.float32)
dst1 = cv2.perspectiveTransform(pts1, M)

## (1, n, 2)
pts2 = np.array([pts], np.float32)
dst2 = cv2.perspectiveTransform(pts2, M)

print("original points: ")
print(pts)

print("mapped points 1: ")
print(dst1)

print("mapped points 2: ")
print(dst2)
