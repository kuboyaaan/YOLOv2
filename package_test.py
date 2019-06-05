import os
import sys
import json
import PIL.Image
import numpy as np
import codecs
#import matplotlib.pyplot as plt
debug = False
shuffle = False

label_dict = {'jabbit': 0}

text = []

with codecs.open(os.path.join('labels', "test.txt"), 'r', 'utf-8', 'ignore') as f:
    text.append(f.read())
text = '\n\n'.join(text)
image_labels = text.split('\n\n')
image_labels = [i.split('\n') for i in image_labels]
image_labels = image_labels[0]
print('check', image_labels)

#print('image_labels', image_labels)
for i, s in enumerate(image_labels[0]):
    dataset_start = s.find('data')
    #print(dataset_start)
    image_labels[0] = s[dataset_start:].split('/')
#print('image_labels', image_labels)
"""for i, s in enumerate(image_labels[1::2]):
    s = s.split(' ')
    box_list = list([])
    for j, box in enumerate(s):
        box_list.append(str(box))

    box_list[0] = label_dict[box_list[0]]
    for k in range(1, 5):
        box_list[k] = int(box_list[k])

    if box_list[2] > box_list[4]:
        box_list[2], box_list[4] = box_list[4], box_list[2]
    if box_list[1] > box_list[3]:
        box_list[1], box_list[3] = box_list[3], box_list[1]
    image_labels[2*i + 1] = box_list"""

images = []
#print(image_labels)
history = np.array(PIL.Image.open(os.path.join('data/VOC/JPEGImages','jabbit21.jpg')), dtype=np.uint8).shape
for i, label in enumerate(image_labels[0::2]):
    img = np.array(PIL.Image.open(os.path.join('data/VOC/JPEGImages','jabbit21.jpg')).resize((300, 300)), dtype=np.uint8)
    #assert(img.shape==history)
    print('img',img.shape)
    images.append(img)
    if debug and i > 100:
        break
    #plt.imshow(img)

images = np.array(images, dtype=np.uint8)
print(images.shape)
"""print(images.shape)

image_labels = [np.array(labels_array) for labels_array in image_labels[1::2]]
image_labels = np.array(image_labels)
#print(image_labels.shape)
#print(image_labels)
if shuffle:
    np.random.seed(13)
    indices = np.arange(len(images))
    np.random.shuffle(indices)
    images, image_labels = images[indices], image_labels[indices]"""

print('Dataset contains {} images'.format(images.shape[0]))
#print('Dataset contains {} image labels'.format(image_labels.shape[0]))
np.savez('test_da_dataset', images=images)
print('Data saved: test_da_dataset.npz')
