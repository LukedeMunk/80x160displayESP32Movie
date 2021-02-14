import cv2
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = "Com"
f = os.path.join(__location__, file + ".mp4")


vidcap = cv2.VideoCapture(f)
success, image = vidcap.read()
count = 0
while success:
  cv2.imwrite(os.path.join(__location__, file + "frame%d.jpg") % count, image)     # save frame as JPEG file      
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1