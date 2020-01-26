import numpy as np
import cv2

image = 'images/example_01.png'

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(image)
cv2.setMouseCallback(image,draw_circle)

cv2.imshow(image, img)
cv2.namedWindow(image)
cv2.setMouseCallback(image, on_click)

def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(lastImage, (x, y), 3, (255, 0, 0), -1)
