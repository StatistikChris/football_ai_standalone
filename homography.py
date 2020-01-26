import numpy as np
import cv2
import matplotlib.pyplot as plt


src_pts = np.array([[50,50],[100,60],[55,105],[110,110]])
dst_pts = np.array([[0,0],[100,0],[0,20],[100,20]])
#dst_pts = src_pts

#print(src_pts)
#print(dst_pts)

h, status = cv2.findHomography(src_pts, dst_pts)

pts = np.float32([[50,50],[100,60],[55,105],[110,110],
[75,55],[52.5,77.5],[105,85],[82.5,107.5] ]).reshape(-1, 1, 2)

results = cv2.perspectiveTransform(pts,h)
results = results.reshape(8,2)

x, y = zip(*results)

print(x)
print(y)


plt.plot(x,y, 'o')
plt.show()
