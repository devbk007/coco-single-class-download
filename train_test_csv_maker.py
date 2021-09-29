import pandas
import os
from required_class import classes, root_dir

root_dir_train = root_dir + \
    classes[0] + "/train"
root_dir_test = root_dir + \
    classes[0] + "/test"

test = []
train = []
for path, subdirs, files in os.walk(root_dir_train):
    for name in files:
        if name.endswith('.jpg'):
            train.append(name)

for path, subdirs, files in os.walk(root_dir_test):
    for name in files:
        if name.endswith('.jpg'):
            test.append(name)

csv_file = str(input("Enter the csv file name of the image class : "))
df = pandas.read_csv(root_dir + "/" + csv_file)
df = df.iloc[:, 1:]

columns = df.columns
df1 = []
df2 = []

train_df = df.loc[df['filename'].isin(train)]
test_df = df.loc[df['filename'].isin(test)]

train_df.to_csv(index=False)
test_df.to_csv(index=False)

train_df.to_csv(root_dir_train + '/train.csv', encoding='utf-8', index=False)
test_df.to_csv(root_dir_test + '/test.csv', encoding='utf-8', index=False)
