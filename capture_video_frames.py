import cv2

#video_filename = 'OpenCV/cutvideo.mp4'
video_filename = 'OpenCV/video2.mp4'

vidcap = cv2.VideoCapture(video_filename)
success,image = vidcap.read()

count = 0
#while success:
while count < 3:
  cv2.imwrite('video_output/frame%d.jpg' % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
