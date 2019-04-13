import csv
import glob
import operator
import os

dir_count = '../../dataset/Google_Landmark_Recognition_2019/train/0/*'
dir_img = '../../dataset/Google_Landmark_Recognition_2019/train/0/'

count_dir = 0
for i in glob.glob(dir_count):
    count_dir += 1
print(count_dir)
a = 0
for i in range(count_dir):
    c = 0
    for j in glob.glob(dir_img + str(i) + '/*/*'):
        c += 1
    print(c)
    a = a + c
print(a)

path = '../../dataset/Google_Landmark_Recognition_2019/train.csv'

search_string = "0000ae056149919f"


def name_chunk(s):
    return os.path.basename(s)[:-4]


files = glob.glob(dir_img + '/0/0/*')

with open(path) as f:
    reader = sorted(csv.reader(f, delimiter=','), key=operator.itemgetter(0))

    i = 0
    for row in reader:
        if name_chunk(files[i]) != row[0]:
            print("error" + str(i))
            break
        if row[0] == search_string:
            print(reader[i][0] + "\n" + search_string, reader[i])
            break
        i += 1
