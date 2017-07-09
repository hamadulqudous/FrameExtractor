import os
import cv2

folder_name = r'01'
if not os.path.exists(folder_name):#will create new folder if not existed
    os.makedirs(folder_name)
print folder_name

vidcap = cv2.VideoCapture('01_01_01_01_00.mp4')
success, count = True, 1
while success:
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  if success:
    cv2.imwrite(folder_name + "//%d.jpg" % count, image)     # save frame as JPEG file
  count += 1
