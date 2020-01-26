# https://stackoverflow.com/questions/28327020/opencv-detect-mouse-position-clicking-over-a-picture/49338267

import numpy as np
import cv2

class LoadImage:
    def loadImage(self):
        self.img=cv2.imread('images/example_01.png')
        cv2.imshow('Test',self.img)

        self.pressedkey=cv2.waitKey(0)

        # Wait for ESC key to exit
        if self.pressedkey==27:
            cv2.destroyAllWindows()


# Start of the main program here
if __name__=="__main__":
    LI=LoadImage()
    LI.loadImage()
