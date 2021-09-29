from os import mkdir
from pycocotools.coco import COCO
from required_class import classes
import requests
import os
import shutil
from time import sleep
from required_class import ann_file


coco = COCO(ann_file)
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=classes)

for i in range(len(classes)):
    if os.path.isdir(classes[i]):
        print("Folder with same class name exists, deleting it........")
        shutil.rmtree(classes[i])
    os.mkdir(classes[i])

count = 0
for i in catIds:

    imgIds = coco.getImgIds(catIds=i)
    images = coco.loadImgs(imgIds)
    print("imgIds: ", imgIds)
    print("images: ", images)

    for im in images:
        print("im: ", im)
        img_data = requests.get(im['coco_url']).content
        sleep(30)
        with open(classes[count] + '/' + im['file_name'], 'wb') as handler:
            handler.write(img_data)
    count = count + 1
