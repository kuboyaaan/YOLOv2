import os
import sys
import json
import PIL.Image
import numpy as np
import codecs

debug = False
shuffle = False

label_dict = {'jabbit': 0}

text = []

with codecs.open(os.path.join('labels', "training.txt"), 'r', 'utf-8', 'ignore') as f:
    text.append(f.read())
text = '\n\n'.join(text)
image_labels = text.split('\n\n')
image_labels = [i.split('\n') for i in image_labels]
image_labels = image_labels[0]
#print('image_labels', image_labels)
for i, s in enumerate(image_labels[0::2]):
    dataset_start = s.find('data')
    image_labels[i*2] = s[dataset_start:].split('/')
for i, s in enumerate(image_labels[1::2]):
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
    image_labels[2*i + 1] = box_list
#print('image_labels', image_labels)
#del image_labels[-1]
images = []
#print(image_labels)
history = np.array(PIL.Image.open(os.path.join(image_labels[0][0], image_labels[0][1], image_labels[0][2], image_labels[0][3])), dtype=np.uint8).shape
for i, label in enumerate(image_labels[0::2]):
    #print('label', label)
    img = np.array(PIL.Image.open(os.path.join(label[0], label[1], label[2], label[3])).resize((300, 300)), dtype=np.uint8)
    #assert(img.shape==history)
    #print('img',img.shape)
    images.append(img)
    if debug and i > 100:
        break

images = np.array(images, dtype=np.uint8)
#print("images.shape", images.shape)
print('image_label', image_labels)
image_labels = [np.array(labels_array) for labels_array in image_labels[1::2]]
image_labels = np.array(image_labels)
#print(image_labels.shape)
#print('image_labels', image_labels)
if shuffle:
    np.random.seed(13)
    indices = np.arange(len(images))
    np.random.shuffle(indices)
    images, image_labels = images[indices], image_labels[indices]
#print('image_labels', image_labels)
print('Dataset contains {} images'.format(images.shape[0]))
print('Dataset contains {} image labels'.format(image_labels.shape[0]))
np.savez('data_dataset', images=images, boxes=image_labels)
print('Data saved: data_dataset.npz')
