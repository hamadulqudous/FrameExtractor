import os
import cv2
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


folder_name = 'Data/'
def total_frames(start_path = folder_name):
    i, j, a, k = 0, 0, 0, 1
    for filenames in os.walk(start_path):

        if a == 0:
            a = 1
        else:
            j += 1
            labFile = 'labels/' + filenames[0].split('/')[1] + '.txt'
            print labFile
            with open(labFile) as f:
                lines = f.readlines()
                label_frames = np.zeros((np.size(lines) - 1, 10)).astype('int')
                for i in range(np.size(lines) - 1):
                    label_frames[i, :] = np.fromstring(lines[i + 1], dtype=int, sep='_')
            label_frames = np.asmatrix(label_frames).astype('int')
            # print label_frames.shape

        for file in filenames[2]:
            i += 1
            path = filenames[0] + '/' + file
            img = cv2.imread(path)
            mf = path.split('.')[0].split('/')[1]
            sf = path.split('.')[0].split('/')[2]
            framelab = path.split('.')[0].split('/')[3]
            # print label_frames[:,0]
            # print framelab
            for m in range(label_frames.shape[0]):
                if label_frames[m, 0] == int(framelab):
                    nam = 'Main Folder: ' + mf + '     Sub Folder: ' + sf + '     Image: ' + framelab + '     Label: ' + str (label_frames[m, 1])
                    print path
                    # plt.figure()
                    # plt.title(nam)
                    # plt.axis('off')
                    # plt.show(plt.imshow(img))
                    # print framelab
                    w, x, y, z = label_frames[m, 3], label_frames[m, 7], label_frames[m, 2], label_frames[m, 4]
                    # print w, x, y, z
                    crop_img = img[w:x, y:z, :]
                    # print crop_img.shape
                    # plt.figure()
                    pat = 'trafficSigns/' + str(label_frames[m, 1]) + '_' + str(k) + '.jpg'
                    # plt.title('Label: ' + str(label_frames[m, 1]))
                    # plt.axis('off')
                    # plt.show(plt.imshow(crop_img))
                    cv2.imwrite(pat, crop_img)
                    k += 1

    return i, j, k
imgs, folders, signs = total_frames()

print 'We have total ', signs, ' traffic signs'


# path = '01_01/86.jpg'
# imgN = path.split('.')[0].split('/')[1]
# img = cv2.imread(path)
# # plt.show(plt.imshow(img))
# print np.shape(img)
# with open('01_01.txt') as f:
#     lines = f.readlines()
#     label_frames = np.zeros((np.size(lines)-1, 10)).astype('int')
#     for i in range(np.size(lines)-1):
#        label_frames[i, :] = np.fromstring(lines[i+1], dtype=int, sep='_')
#
# det = label_frames[label_frames[:, 0] == int(imgN)]
# k = 1
# print det.shape
# for i in range(det.shape[0]):
#     w, x, y, z = det[i, 3], det[i, 7], det[i, 2], det[i, 4]
#     print w, x, y, z
#     crop_img = img[w:x, y:z, :]
#     print crop_img.shape
#     plt.figure()
#     pat = 'trafficSigns/' + str(det[i, 1]) + '_' + str(k) + '.jpg'
#     plt.title('Label: ' + str(det[i, 1]))
#     plt.axis('off')
#     # plt.show(plt.imshow(crop_img))
#     cv2.imwrite(pat, crop_img)
#     k += 1
