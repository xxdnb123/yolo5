import os
import random
import shutil

pathfrom = r"D:/yanbo/yolov5-master/yolov5-master/data/images"
trainpath = r"D:/yanbo/yolov5-master/yolov5-master/data/ImageSets"
pathDir = os.listdir(pathfrom)  # 取图片的原始路径
random.seed(1)
filenumber = len(pathDir)  # 原文件个数
rate = 0.2  # 抽取的验证集的比例，占总数据的多少
picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
sample = random.sample(pathDir, picknumber)  # 随机选取需要数量的样本图片
print(sample)
list_len = len(sample)
print(list_len)
trainwrite = open(trainpath + '/' + 'train.txt', 'w')
valw=open(trainpath+ '/' + 'val.txt', 'w')
pathDir2 = os.listdir(pathfrom)
for i in sample:
    trainwrite.write('data/images/'+i+'\n')
trainwrite.close()
for i in pathDir2:
    if i not in sample:
        valw.write('data/images/'+i+'\n')
# for flie_name in list:
#     path_img = os.path.join(input1, flie_name + '.jpg')
#     shutil.move(path_img, save1)
#     path_lab = os.path.join(input2, flie_name + '.txt')
#     shutil.move(path_lab, save2)
