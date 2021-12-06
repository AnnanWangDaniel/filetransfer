from shutil import copy

with open('./split_data/gtav_split_train.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "/home/wangannan/URECA21/datasets/GTAV/images/{img}".format(img = img_name)
        dst = "/home/wangannan/URECA21/datasets/GTAV/images/train/folder/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_train.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "/home/wangannan/URECA21/datasets/GTAV/labels/{img}".format(img = img_name)
        dst2 = "/home/wangannan/URECA21/datasets/GTAV/labels/train/folder/"
        copy(src2, dst2)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_test.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "/home/wangannan/URECA21/datasets/GTAV/images/{img}".format(img = img_name)
        dst = "/home/wangannan/URECA21/datasets/GTAV/images/test/folder/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_test.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "/home/wangannan/URECA21/datasets/GTAV/labels/{img}".format(img = img_name)
        dst2 = "/home/wangannan/URECA21/datasets/GTAV/labels/test/folder/"
        copy(src2, dst2)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_val.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src = "/home/wangannan/URECA21/datasets/GTAV/images/{img}".format(img = img_name)
        dst = "/home/wangannan/URECA21/datasets/GTAV/images/valid/folder/"
        copy(src, dst)
        count = count + 1
    print(count)

with open('./split_data/gtav_split_val.txt', encoding='utf8') as f:
    count = 0
    for line in f:
        img_name = line.strip()
        src2 = "/home/wangannan/URECA21/datasets/GTAV/labels/{img}".format(img = img_name)
        dst2 = "/home/wangannan/URECA21/datasets/GTAV/labels/valid/folder/"
        copy(src2, dst2)
        count = count + 1
    print(count)
