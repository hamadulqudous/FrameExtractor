import os
import cv2
import csv
import random as rm
import numpy as np
import pandas as pd

folder_name = 'Data'
def total_frames(start_path = folder_name):
    i, j, k = 0, 0, 0
    for filenames in os.walk(start_path):
        for file in filenames[2]:
            i += 1
    return i
size = total_frames()
size2 = 224*224*3

def get_images(start_path = folder_name, x = size):
    images, i, j, z= np.zeros((x, 224, 224, 3)), 0, 0, 224*224*3
    data = np.zeros((x, z))
    label = np.zeros(x)
    print label.shape
    for filenames in os.walk(start_path):
        if j >= 1:
            fold = filenames[0].split('/')[1:2]
            lab = 'label/' + str(fold)[2:7] + '.csv'
            labs = np.asarray(pd.read_csv(lab)['Label'])
        j += 1
        for file in filenames[2]:
            index = int (file.split('.')[0]) -1
            label[i] = labs[index]
            name = filenames[0] + '/' + file
            img = cv2.imread(name)
            resized_image = np.atleast_3d(cv2.resize(img, (224, 224)))
            data[i, :] = resized_image.reshape(z)
            i += 1
    return label, data

l, d = get_images()
print l.shape, d.shape


nums = [x for x in range(15000)]
rm.shuffle(nums)

with open('label_1.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(500):
        writer.writerow([l[nums[i]]])

with open("data_1.csv", "wb") as f:
     writer = csv.writer(f, delimiter=',')
     writer.writerows(d[nums[0:500], :])
