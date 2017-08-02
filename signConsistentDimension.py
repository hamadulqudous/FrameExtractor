import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder_name = 'trafficSigns/'
folder_name2 = 'processed/'
def total_frames(start_path = folder_name):
    i, j, k = 0, 0, 0
    for filenames in os.walk(start_path):
        for file in filenames[2]:
            i += 1
    return filenames[2], i

frames, size =  total_frames()
data = np.zeros((size, 224, 224, 3))
label = np.zeros(size).astype('int')

for i in range(size):
    path = folder_name + frames[i]
    path2 = folder_name2 + frames[i]
    img = cv2.imread(path)
    d1 = img.shape[0]
    d2 = img.shape[1]
    c1 = np.divide((data.shape[1] - img.shape[0]), 2)
    c2 = np.divide((data.shape[2] - img.shape[1]), 2)
    print c1, c2, img.shape[0], img.shape[1]
    data[i, c1: c1 + d1, c2: c2 + d2, :] = img
    plt.show(plt.imshow(data[i, :, :, :]))
    label[i] = int (frames[i].split('_')[0])
    # print ('having label: ', label[i])
    # cv2.imwrite(path2, data[i])








