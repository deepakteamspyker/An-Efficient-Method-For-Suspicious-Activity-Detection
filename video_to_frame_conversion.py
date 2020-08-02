import cv2
import numpy as np
import os


cap = cv2.VideoCapture('input.avi')

try:
    if not os.path.exists('All Frames'):
        os.makedirs('All Frames')
except OSError:
    print ('Error: Creating directory of data')
currentFrame = 0
while(True):

    ret, frame = cap.read()
    name = './All Frames/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    currentFrame += 1
cap.release()
cv2.destroyAllWindows()
