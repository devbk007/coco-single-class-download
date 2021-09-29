import os
os.system('python ./download_image.py')
os.system('python ./download_annotations.py')
os.system('python ./split_train_test.py')
os.system('python ./train_test_csv_maker.py')
print("Process is complete............")
exit
