import json
import os
from PIL import Image
import re
import shutil

#
# # i=0
# while i<=34525:
#     imgpathfrom=r"D:/yanbo/yolov5-master/mydata/images/train"
#     imgpathto=r"D:/yanbo/yolov5-master/mydata/images/test"
#     labelpathfrom = r"D:/yanbo/yolov5-master/mydata/labels/train"
#     labelpathto = r"D:/yanbo/yolov5-master/mydata/labels/test"
#     imgpathfrom += '/' + str(i) + '.jpg'
#     imgpathto += '/' + str(i) + '.jpg'
#     labelpathfrom += '/' + str(i) + '.txt'
#     labelpathto += '/' + str(i) + '.txt'
#     shutil.move(imgpathfrom,imgpathto)
#     shutil.move(labelpathfrom,labelpathto)
#     i+=1
# pathfrom = r"D:/yanbo/yolov5-master/yolov5-master/data/labels/train"
# pathto = r"D:/yanbo/yolov5-master/yolov5-master/data/labels"
# for fp in os.listdir(pathfrom):
#     shutil.move(pathfrom + '/' + fp, pathto + '/' + fp)
# with open('D:/yanbo/无人机检测与追踪/无人机检测与追踪/result/01_2192_0001-1500/000306.txt','r') as fn:
#     ls=fn.read().split(' ')
#     for i in ls:
#         print(i)
dir1 = os.listdir('D:/yanbo/无人机检测与追踪/无人机检测与追踪/result')
dir2 = os.listdir('D:/yanbo/无人机检测与追踪/无人机检测与追踪/test')
for wenjianjia in dir1:
    jsontxt = {"res": []}
    dir1_1 = os.listdir('D:/yanbo/无人机检测与追踪/无人机检测与追踪/result' + "/" + wenjianjia)
    # print(dir1_1)
    dirimg = os.listdir('D:/yanbo/无人机检测与追踪/无人机检测与追踪/test' + "/" + wenjianjia)
    for img in dirimg:
        temp = img.split('.')[0]
        temp2 =temp+ ".txt"
        temp3 =temp+".txt"
        # dir1_2=os.listdir(D:/yanbo/无人机检测与追踪/无人机检测与追踪/result' + "/" + wenjianjia)
        if temp3 in dir1_1:
            with open('D:/yanbo/无人机检测与追踪/无人机检测与追踪/result' + "/" + wenjianjia + "/" + temp2) as txtnei:
                strneil = txtnei.read().split('\n')
                strnei =strneil[0]
                strnei=strnei.split(" ")
                img = Image.open('D:/yanbo/无人机检测与追踪/无人机检测与追踪/test' + "/" + wenjianjia + "/" + temp + ".jpg")

                listt = []
                x = strnei[1]


                y = strnei[2]
                width1 = strnei[3]
                length1 = strnei[4]
                length1=length1.split('\\')[0]
                print(length1)
                print("\n")
                listt.append(float(x) * int(img.width))
                listt.append(float(y) * int(img.height))
                listt.append(float(width1) * int(img.width))
                listt.append(float(length1) * int(img.height))
                jsontxt['res'].append(listt)
        else:
            jsontxt['res'].append([])
    baocun = open('D:/yanbo/无人机检测与追踪/无人机检测与追踪/jieguo/'+wenjianjia+".json", 'w')
    json.dump(jsontxt,baocun)
    baocun.close()