# https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture/49338267

import numpy as np
import cv2

image = 'video_output/frame0.jpg'
output_file = 'output/coords.txt'
#output_file = 'output/test.txt'
pos_list = []

radius = 10

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),radius,(255,0,0),-1)
        mouseX,mouseY = x,y
        pos_list.append([mouseX, mouseY])


#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread(image, cv2.IMREAD_COLOR)
cv2.namedWindow(image)
cv2.setMouseCallback(image,draw_circle)

while(1):
    with open(output_file,'w+') as file:

        cv2.imshow(image,img)
        k = cv2.waitKey(20) & 0xFF

        if k == 27:
            #pos_list = np.array(pos_list)
            file.write(str(pos_list))
            break

        elif k == ord('a'):
            print(mouseX,mouseY)
