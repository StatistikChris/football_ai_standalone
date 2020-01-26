from tkinter import *
from tkinter.ttk import Combobox,  Checkbutton
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np

image_path = 'video_output/frame0.jpg'

positions = []

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y
        positions.append([x,y])

def double_click(event, x, y, flags, param):
    mouseX,mouseY = x,y
    cv2.imshow("image", image)


def clicked():
    global image
    image = cv2.imread(image_path)

    #clone = image.copy()
    #cv2.namedWindow("ROI")
    cv2.imshow("image", image)
    cv2.setMouseCallback("image", draw_circle)

    while(1):
        cv2.imshow('image',image)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            np.savetxt("positions.csv", positions, delimiter=",")
            break
        elif k == ord('a'):
            print(mouseX,mouseY)

    # close all open windows
    cv2.destroyAllWindows()






window = Tk()
window.title('welcome to the best program in the world')

# define size of window
window.geometry('1000x800')


# adding a button widget
btn = Button(window, text ='click me to open image', bg='orange', fg='green',
    command = clicked)
btn.grid(column=2, row=0)

window.mainloop()
