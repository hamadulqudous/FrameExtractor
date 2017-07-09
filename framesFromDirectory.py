import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folder_name = '01/'

def get_frames(start_path = folder_name):
    for filenames in os.walk(start_path):
        filenames
    return filenames[2]
total_Frames = get_frames()
data = np.zeros((224, 224, 3, np.size(total_Frames)))
for frame in total_Frames:
    data[:, :, :, int(frame.split('.')[0])-1] = cv2.resize(cv2.imread(folder_name+frame), (224, 224)).astype(np.float32)
    # plt.show(plt.imshow(img))
    # print int(frame.split('.')[0]) - 1
labels = np.asarray(pd.read_csv('01.csv')['Label'])

print data.shape, labels.shape
