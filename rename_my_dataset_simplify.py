# ！/usr/bin/env python
# -*- coding: utf-8 -*-
import os


img_path='/Users/lyl666/Desktop/img_test'


img_filelist = os.listdir(img_path)
# xml_filelist = os.listdir(xml_path)
print(type(os.path.splitext(img_filelist[0])[0]))


def rename():
    i = 0
    j = 0

    file_img_type = '.jpg'
    file_xml_type = '.xml'
    count = 0
    for item_i in img_filelist:
        for item_x in xml_filelist:
            if os.path.splitext(item_i)[0] == os.path.splitext(item_x)[0]:
                old_img_file = os.path.join(img_path, item_i)
                old_xml_file = os.path.join(xml_path, item_x)
                new_img_file = os.path.join(img_path, str(int(i+1)) + file_img_type)
                new_xml_file = os.path.join(xml_path, str(int(i+1)) + file_xml_type)

                os.rename(old_img_file, new_img_file)
                os.rename(old_xml_file, new_xml_file)
                print("旧—img-文件:"+str(item_i)+"新-img-文件:"+str(int(i+1))+file_img_type)
                print("旧-xml-文件:"+str(item_x)+"新-xml-文件:"+str(int(i+1))+file_xml_type+'\n')
                count += 1
                j+=1   #作为每一轮循环有文件被修改的标志
            else:
                pass
        if j!=0:
            i += 1
        j = 0
    print("被修改的文件数为：" + str(count))

rename()