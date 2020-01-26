from tkinter import *
from tkinter.ttk import Combobox,  Checkbutton
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np
import os
#from standalone_source import click_to_open_video_file, click_to_detect_players, click_on_corners, click_to_transform_coords
from standalone_source import *



window = Tk()
window.title('welcome to the best program in the world')
# define size of window
window.geometry('1000x800')

lbl_0 = Label(window , text='1. Hello, please choose a folder for all relevant outputs', font=('Arial Bold', 11))
lbl_0.grid(column=0, row=0)
# adding a button widget
btn_0 = Button(window, text ='click me to specify output folder', bg='orange', fg='green',
    command = click_to_specify_directory)
btn_0.grid(column=0, row=1)

lbl_1 = Label(window , text='2. Hello, please choose a video file from your hard disk', font=('Arial Bold', 11))
lbl_1.grid(column=0, row=2)
# choose video file from local directory
btn_1 = Button(window, text ='Choose file for processing', bg='purple', fg='green',
    command = click_to_open_video_file)
btn_1.grid(column=0, row=3)

lbl_2 = Label(window , text='3. After choosing video file, process player detection.', font=('Arial Bold', 11))
lbl_2.grid(column=0, row=4)
# run player detection on chosen video file
btn_2 = Button(window, text ='click me to detect players', bg='orange', fg='green',
    command = click_to_detect_players)
btn_2.grid(column=0, row=5)

lbl_3 = Label(window , text='4. Now capture video frame to draw on it.', font=('Arial Bold', 11))
lbl_3.grid(column=0, row=6)
# extract frame from video ...
btn_3 = Button(window, text ='click me to capture frames', bg='orange', fg='green',
    command = click_to_capture_frames)
btn_3.grid(column=0, row=7)

lbl_4 = Label(window , text='5. Now choose four corners on the field.', font=('Arial Bold', 11))
lbl_4.grid(column=0, row=8)
# ... and click on corners
btn_4 = Button(window, text ='click me choose four corners', bg='orange', fg='green',
    command = click_on_corners)
btn_4.grid(column=0, row=9)


lbl_5 = Label(window , text='6. Finally transoform player coords to new perspective.', font=('Arial Bold', 11))
lbl_5.grid(column=0, row=10)
# map players to rectangle
btn_5 = Button(window, text ='click me to transform coords to rectangle', bg='orange', fg='green',
    command = click_to_transform_coords)
btn_5.grid(column=0, row=11)


window.mainloop()
