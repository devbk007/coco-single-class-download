from required_class import classes
import os
import numpy as np
import shutil
from required_class import test_ratio
from required_class import root_dir

classes_dir = classes
classes_dir = classes

for cls in classes_dir:
    os.makedirs(root_dir + '/' + cls + '/train/')
    os.makedirs(root_dir + '/' + cls + '/test/')

src = root_dir + '/' + classes_dir[0]

allFileNames = os.listdir(src)
np.random.shuffle(allFileNames)
train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                           [int(len(allFileNames) * (1 - test_ratio))])


train_FileNames = [src+'/' + name for name in train_FileNames.tolist()]
test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

print("*****************************")
print('Total images: ', len(allFileNames))
print('Training: ', len(train_FileNames))
print('Testing: ', len(test_FileNames))
print("*****************************")


for name in train_FileNames:
    for i in classes:
        try:
            if name.endswith('.jpg'):
                shutil.move(name, root_dir + '/' + i + '/train/')
        except:
            print("Permission Error")

for name in test_FileNames:
    for i in classes:
        try:
            if name.endswith('.jpg'):
                shutil.move(name, root_dir + '/' + i + '/test/')
        except:
            print("Permission Error")
print("Copying Done!")
