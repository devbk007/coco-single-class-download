root_dir = "<Enter the root path>"
ann_file = "<Enter annotation json file path>"

names = str(input("Enter the required class : "))
classes = names.split('.')

print()
test_ratio = float(input("Enter the test ratio, eg: if 20%, enter 0.2 : "))
