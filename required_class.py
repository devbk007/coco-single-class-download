root_dir = "F:\learn\ineuron\CNN\coco_download_classes"
ann_file = "annotations_trainval2017\instances_train2017.json"

names = str(input("Enter the required class : "))
classes = names.split('.')

print()
test_ratio = float(input("Enter the test ratio, eg: if 20%, enter 0.2 : "))
