import csv
import numpy as np

with open('01_01.txt') as f:
    lines = f.readlines()
    label_frames = np.zeros((np.size(lines), 10)).astype('int')
    for i in range(np.size(lines)-1):
       label_frames[i, :] = np.fromstring(lines[i+1], dtype=int, sep='_')

labels = np.zeros((300, 2)).astype('int')
fr = [x for x in range(300)]
fr = np.array(fr).astype('int')
labels[label_frames[:, 0]-1, 1] = 1
labels[fr[:], 0] = fr[:]


with open('01.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    writer.writerow(['Frame'] + ['Label'])
    for i in range(300):
        writer.writerow([labels[i, 0]] + [labels[i, 1]])
