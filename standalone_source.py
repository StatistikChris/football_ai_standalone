import cv2
import numpy as np
import os
from tkinter import filedialog
from pathlib import Path

import read_player_coords
from read_player_coords import read_coords
import transform_source
from transform_source import read_corners, transform, order_points

def click_to_specify_directory():
    # filedialog
    global directory_name
    directory_name = filedialog.askdirectory()

def click_to_open_video_file():
    # filedialog
    global video_filename
    video_filename = filedialog.askopenfilename(filetypes = (("Video files","*.mp4"),("all files","*.*")))
    #string = 'You have chosen the following file: "{}" '.format(video_filename)
    #lbl.configure(text=string)

def click_to_detect_players():
    #Reading the video
    #vidcap = cv2.VideoCapture('OpenCV/cutvideo.mp4')
    vidcap = cv2.VideoCapture(video_filename)
    success,image = vidcap.read()
    count = 0
    success = True
    idx = 0
    #output_file = 'output/player_coords.txt'
    output_file = directory_name + "/player_coords.txt"

    coord_list = []
    # context manager for output file
    with open(output_file,'w+') as file:
        #Read the video frame by frame
        while success:
            #converting into hsv image
            hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            #green range
            lower_green = np.array([40,40, 40])
            upper_green = np.array([70, 255, 255])
            #blue range
            lower_blue = np.array([110,50,50])
            upper_blue = np.array([130,255,255])
            #Red range
            lower_red = np.array([0,31,255])
            upper_red = np.array([176,255,255])
            #white range
            lower_white = np.array([0,0,0])
            upper_white = np.array([0,0,255])

            #Define a mask ranging from lower to uppper
            mask = cv2.inRange(hsv, lower_green, upper_green)
            #Do masking
            res = cv2.bitwise_and(image, image, mask=mask)
            #convert to hsv to gray
            res_bgr = cv2.cvtColor(res,cv2.COLOR_HSV2BGR)
            res_gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

            #Defining a kernel to do morphological operation in threshold image to
            #get better output.
            kernel = np.ones((13,13),np.uint8)
            thresh = cv2.threshold(res_gray,127,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

            #find contours in threshold image
            contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            prev = 0
            font = cv2.FONT_HERSHEY_SIMPLEX
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                #Detect players
                ratio = 1
                min_size = 10
                if(h>=(ratio)*w):
                    if(w>min_size and h>= min_size):
                        idx += 1
                        player_img = image[y:y+h,x:x+w]
                        player_hsv = cv2.cvtColor(player_img,cv2.COLOR_BGR2HSV)
                        #If player has white jersy
                        mask1 = cv2.inRange(player_hsv, lower_white, upper_white)
                        res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                        res1 = cv2.cvtColor(res1,cv2.COLOR_HSV2BGR)
                        res1 = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
                        nzCount = cv2.countNonZero(res1)
                        #If player has red jersy
                        mask2 = cv2.inRange(player_hsv, lower_red, upper_red)
                        res2 = cv2.bitwise_and(player_img, player_img, mask=mask2)
                        res2 = cv2.cvtColor(res2,cv2.COLOR_HSV2BGR)
                        res2 = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
                        nzCountred = cv2.countNonZero(res2)

                        # write coords to txt file
                        coord_string = str(count) + ',' + str(x+w) + ',' + str(y) + ','
                        file.write(coord_string)
                        #coord_list.append([count,x+w,y])


                        if(nzCount >= 2):
                        	#Mark white jersy players as Argentina
                        	cv2.putText(image, 'Argentina', (x-2, y-2), font, 0.8, (255,0,0), 2, cv2.LINE_AA)
                        	cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)
                        else:
                        	pass
                        if(nzCountred>=20):
                        	pass

                        	#Mark red jersy players as belgium
                        	#cv2.putText(image, 'Belgium', (x-2, y-2), font, 0.8, (0,0,255), 2, cv2.LINE_AA)
                        	#cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),3)
                        else:
                        	pass

                if((h>=1 and w>=1) and (h<=30 and w<=30)):
                    player_img = image[y:y+h,x:x+w]
                    player_hsv = cv2.cvtColor(player_img,cv2.COLOR_BGR2HSV)
                    #white ball  detection
                    mask1 = cv2.inRange(player_hsv, lower_white, upper_white)
                    res1 = cv2.bitwise_and(player_img, player_img, mask=mask1)
                    res1 = cv2.cvtColor(res1,cv2.COLOR_HSV2BGR)
                    res1 = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
                    nzCount = cv2.countNonZero(res1)

                    #if(nzCount >= 3):
                    #    cv2.putText(image, 'football', (x-2, y-2), font, 0.8, (0,255,0), 2, cv2.LINE_AA)
                    #    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

            frame_path = directory_name + "/Cropped/frame%d.jpg" % count
            cv2.imwrite(frame_path, res)
            #cv2.imwrite("/Cropped/frame%d.jpg" % count, res)
            count += 1
            cv2.imshow('Match Detection',image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            success,image = vidcap.read()

        vidcap.release()
        cv2.destroyAllWindows()


def click_to_capture_frames():
    vidcap = cv2.VideoCapture(video_filename)
    success,image = vidcap.read()


    Path(directory_name + '/video_output').mkdir(parents=True, exist_ok=True)

    count = 0
    #while success:
    while count < 3:
        video_path = directory_name + '/video_output/frame%d.jpg' % count
        cv2.imwrite(video_path, image)
        #cv2.imwrite('video_output/frame%d.jpg' % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


def click_on_corners():
    image = directory_name + '/video_output/frame0.jpg'
    output_file = directory_name + '/coords.txt'
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
                cv2.destroyAllWindows()
                break

            elif k == ord('a'):
                print(mouseX,mouseY)


def click_to_transform_coords():

    # get coords of detected players
    player_coords_file = directory_name + '/player_coords.txt'
    #player_coords_file = 'output/test.txt'
    coords = read_coords(player_coords_file)
    coords = np.reshape(coords , (-1,3))

    # get coords of the four corners
    corners_file = directory_name + '/coords.txt'
    corners = read_corners(corners_file)
    corners = order_points(corners)
    mapping = transform(corners)

    output_file = directory_name + '/mapped_player_coords.txt'

    # old coords have to be mapped to new coords element by element
    new_coords = []

    for c in coords:
        f, x ,y = c # frame, x-coord, y-coord
        point = [x,y] # mapping functions expects 2dim input

        new_point = mapping.coord_transform(point)
        new_coords.append(f) # append elements to list of new_coords
        new_coords.append(new_point[0])
        new_coords.append(new_point[1])

    with open(output_file,'w+') as file:
        file.write(str(new_coords))
