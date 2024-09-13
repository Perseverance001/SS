"""
# VOC数据集 转 YOLO数据集 格式
"""


import xml.etree.ElementTree as ET
import os
import random

classes = ["entrance", "missile_silos", "oid_depot", "helicopter", "military_aircraft",
           "hangars_up","hangars_down", "vehicle", "ammunition_depot","helipad"]

# 划分比率
TRAIN_RATIO = 80

#清除隐藏文件
def clear_hidden_files(path):
    '''
    清除指定路径中的隐藏文件 :param path: 要清除的路径 :return: 无
    '''
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)
#清空文件夹
def clear_files(path):
    '''
    清除指定文件夹中的文件
    '''
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            os.remove(abspath)
        else:
            clear_files(abspath)

# size是原图的宽和高
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

#从xml文件中读取信息，并转换成yolo格式
def convert_annotation(who,image_id):
    # Annotations = ['data-HQ/Annotations', 'data-WQ/Annotations', 'data-GYM/Annotations', 'data-SZT/Annotations',
    #                'data-TXR/Annotations']  # 注解文件夹
    in_file = open(f'../data-{who}/Annotations/{image_id}.xml', 'rb')
    out_file = open('YOLOLabels/%s.txt' % image_id, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()

#当前路径
wd = os.getcwd()

# (创建文件夹存储yolo格式标签)
yolo_labels_dir = os.path.join(wd, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
    os.mkdir(yolo_labels_dir)
clear_files(yolo_labels_dir)
print('YOLOLabels文件夹已清空')

# 生成yolov5_train.txt, yolov5_val.txt
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')

#定义组内成员文件夹名
# partner=['HQ','WQ','GYM','SZT','TXR']
partner=['HQ'] #测试

for p in partner:
    image_dir=f"../data-{p}/JPEGImages/"
    annotation_dir=f"../data-{p}/Annotations/"
    list_imgs = os.listdir(image_dir)  # list image_one files
    prob = random.randint(1, 100)
    print("Probability: %d" % prob)
    for i in range(0, len(list_imgs)):
        path = os.path.join(image_dir, list_imgs[i])
        if os.path.isfile(path):
            image_path = image_dir + list_imgs[i]
            voc_path = list_imgs[i]
            (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
            (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
            annotation_name = nameWithoutExtention + '.xml'
            annotation_path = os.path.join(annotation_dir, annotation_name)
            label_name = nameWithoutExtention + '.txt'
            #
            label_path = os.path.join(yolo_labels_dir, label_name)
        prob = random.randint(1, 100)
        print("Probability: %d" % prob)
        #将YOLOLabels里的数据按比例写入train val（images labels下）文件夹
        if (prob < TRAIN_RATIO):  # train dataset
            if os.path.exists(annotation_path):
                train_file.write(image_path + '\n')
                convert_annotation(p,nameWithoutExtention)  # convert label
        else:  # val dataset
            if os.path.exists(annotation_path):
                #写入路径信息、
                test_file.write(image_path + '\n')
                #转换成yolo格式后写入
                convert_annotation(p,nameWithoutExtention)  # convert label
train_file.close()
test_file.close()

#链接train.py
# os.system('train.py')

