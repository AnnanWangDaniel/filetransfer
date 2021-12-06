from shutil import copy

with open('./split_data/gtav_split_train.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "D:/datasets/gtav/images/{img}".format(img = img_name)
        dst = "D:/datasets/gtav/images/train/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_train.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "D:/datasets/gtav/labels/{img}".format(img = img_name)
        dst2 = "D:/datasets/gtav/labels/train/"
        copy(src2, dst2)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_test.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "D:/datasets/gtav/images/{img}".format(img = img_name)
        dst = "D:/datasets/gtav/images/test/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_test.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "D:/datasets/gtav/labels/{img}".format(img = img_name)
        dst2 = "D:/datasets/gtav/labels/test/"
        copy(src2, dst2)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_val.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "D:/datasets/gtav/images/{img}".format(img = img_name)
        dst = "D:/datasets/gtav/images/valid/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_val.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "D:/datasets/gtav/labels/{img}".format(img = img_name)
        dst2 = "D:/datasets/gtav/labels/valid/"
        copy(src2, dst2)
        count = count + 1
    print(count)