# ！/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from xml.dom import minidom
import math


# xml_path='/Users/lyl666/Desktop/xml_test'
#
# file_xml_list=os.listdir(xml_path)
# print(file_xml_list)
# #通过这个函数批量获得xml文件
# xml_node_list=[]
# file_path_list=[]
# def get_xml_files():
#
#     # file_xml_type='.xml'
#
#     for item in file_xml_list:
#         file_path=os.path.join(xml_path,item)
#         dom=minidom.parse(file_path)
#         root=dom.documentElement
#         xml_node_list.append(root)
#         file_path_list.append(file_path)







#对每一个xml文件获取其相关的node参数：w_node，h_node，angle_node
def get_three_node(file_path_list):
    pass
# File = open('/Users/lyl666/Desktop/2.xml','r')
# lines = File.readlines()
# File.close()
# print(len(lines))
# print(lines)

# dom=minidom.parse(xml_path)
#得到元素对象
# root=dom.documentElement
#获取对应标签的子元素对象
# name=root.getElementsByTagName('angle')[0].childNodes[0].data
# print(name)



# angle_node=root.getElementsByTagName('angle')[0].childNodes[0]
# print(root.getElementsByTagName('angle')[0].childNodes[0].data)
# print(type(root.getElementsByTagName('angle')[0].childNodes[0].data))
# print(root.getElementsByTagName('angle')[1].childNodes[0].data)
# angle_node=root.getElementsByTagName('angle')
# w_node=root.getElementsByTagName('w')
# h_node=root.getElementsByTagName('h')
# print(angle_node.length)
#
# print("接下来打印某一文件的所有angle元素：")




def xml_change(file_path_list,w_node,h_node,angle_node):
    for file_item in file_path_list:
        for i in range(angle_node.length):
            w_node_data=w_node[i].childNodes[0].data
            h_node_data=h_node[i].childNodes[0].data



            angle_node_data=angle_node[i].childNodes[0].data
            print('旧的w和h以及angle',w_node_data,h_node_data,angle_node_data)
    #print("原始的w,h,angle：" + " " + str(w_node_data) + " " + str(h_node_data) + " " + str(angle_node_data))
    # w_node_data_1=int(w_node_data)
    # h_node_data_1=int(h_node_data)
    # angle_node_data_1=int(angle_node_data)
            h_node[i].firstChild.data=abs(math.sin(float(angle_node_data)))*math.floor(float(w_node_data))+abs(math.cos(float(angle_node_data)))*math.floor(float(h_node_data))
            print('angle的弧度为：',math.radians(float(angle_node_data)))
            print('angle的真实弧度为:',float(angle_node_data))
            print('sin_angle为：',abs(math.sin(float(angle_node_data))))
            print('cos_angle为：',abs(math.cos(float(angle_node_data))))
            w_node[i].firstChild.data=abs(math.sin(float(angle_node_data)))*math.floor(float(h_node_data))+abs(math.cos(float(angle_node_data)))*math.floor(float(w_node_data))
            print('新的h',h_node[i].firstChild.data)
            print('新的w',w_node[i].firstChild.data)
            with open(file_item,'w',encoding='UTF-8') as fh:
                dom.writexml(fh)
                print('写入属性OK!')
            fh.close()
    #检查刚刚写入的文件数据
     #         dom = minidom.parse(xml_path)
     # # 得到元素对象
     #         root = dom.documentElement
            # angle_node = root.getElementsByTagName('angle')
            # w_node = root.getElementsByTagName('w')
            # h_node = root.getElementsByTagName('h')
            # w_node_data = w_node[i].childNodes[0].data
            # h_node_data = h_node[i].childNodes[0].data
            # angle_node_data = angle_node[i].childNodes[0].data
    print("ok")
    #print("更新后的w,h,angle："+" "+str(w_node_data)+" "+str(h_node_data)+" "+str(angle_node_data))




xml_path='/Users/lyl666/Desktop/xml_test_2'
file_xml_list=os.listdir(xml_path)
# print(file_xml_list)
# print(len(file_xml_list))
# for i in range(len(file_xml_list)):
#     print(i,file_xml_list[i])
#     print(os.path.join(xml_path,file_xml_list[i]))


j=0
for i in range(len(file_xml_list)):
    xml_full_path=os.path.join(xml_path,file_xml_list[i])
    print(os.path.join(xml_path,file_xml_list[i]))
    dom=minidom.parse(xml_full_path)
    root=dom.documentElement
    angle_node=root.getElementsByTagName('angle')
    w_node=root.getElementsByTagName('w')
    h_node=root.getElementsByTagName('h')
    # print(w_node,h_node,angle_node)
    # xml_change(w_node, h_node, angle_node)
    xml_change([xml_full_path],w_node,h_node,angle_node)
    # if file_xml_list[i]=='video_20200908_152423_196.xml':
    #     print('###############')
    #     print(file_xml_list[i])
    j+=1
    print(j)
  
# angle_node.nodeValue=100
# print(angle_node.nodeValue)
# with open(xml_path,'w',encoding='UTF-8') as fh:
#     dom.writexml(fh)
#     print('写入属性OK！')





