import os
import json
from PIL import Image
import re
import shutil

pathfor = r"D:/yanbo/无人机检测与追踪/无人机检测与追踪/train"
count = 0
imgpath = r"D:/yanbo/yolov5-master/mydata/images/train"
labelpath = r"D:/yanbo/yolov5-master/mydata/labels/train"
for file_name in os.listdir(pathfor):
    print(file_name)
    path2 = pathfor + "/" + str(file_name)
    for fn in os.listdir(path2):
        if re.search('json', fn) is None:
            img = Image.open(path2 + '/' + fn)
            # print(img.size)
            path = pathfor + '/' + file_name + "/IR_label.json"
            with open(path, 'r', encoding='utf-8') as fp:
                data_str = fp.read()
                data_dict = json.loads(data_str)
                typelist = data_dict['exist']
                poslist = data_dict['gt_rect']
                # print(typelist)
                # print(poslist)
                i = 0
                # path_save = r"D:/yanbo/无人机检测与追踪/无人机检测与追踪/train/new2_train/label"

                path_pic = path2 + '/' + fn
                path_aim = labelpath + '/' + str(count) + ".txt"
                file = open(path_aim, 'w')
                # path_pic2 = path_pic + path_o + str(i + 1) + ".jpg"
                pathnew = imgpath + '/' + str(count) + ".jpg"
                img = Image.open(path_pic)
                file.write(str(typelist[i]))
                x_center = poslist[i][0] + poslist[i][2] / 2
                y_center = poslist[i][1] + poslist[i][3] / 2
                x_center = x_center / img.width
                y_center = y_center / img.height
                Twidth = poslist[i][2] / img.width
                Theight = poslist[i][3] / img.height
                file.write(' ')
                file.write(str(x_center))
                file.write(' ')
                file.write(str(y_center))
                file.write(' ')
                file.write(str(Twidth))
                file.write(' ')
                file.write(str(Theight))
                i += 1
                img.close()
                shutil.move(path_pic, pathnew)
                count += 1
        else:
            continue
