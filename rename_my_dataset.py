import os

# class BatchName():
#     def __init__(self):
#         self.path=os.getcwd()
#         print(self.path)
#
#
# pwd_path=BatchName()
#print(os.path.abspath(__file__))

#print(os.path.split(os.path.abspath(__file__))[1])
# for item in (os.getenv('PATH').split(':')):
#     print(item+'\n')
#print(os.path.splitext(os.path.split(os.path.abspath(__file__))[1])[0])
#print(os.path.dirname(os.path.abspath(__file__)))
img_names_jpg=os.listdir('/Users/lyl666/Desktop/img_test')
xml_names_jpg=os.listdir('/Users/lyl666/Desktop/xml_test')
print(len(img_names_jpg),len(xml_names_jpg))
print(os.path.splitext('/Users/lyl666/Desktop/img_test'))
img_names=[]
xml_names=[]
# print(os.path.splitext(img_names_jpg[0])[0])
# img_names.append(os.path.splitext(img_names_jpg[0])[0])
print('jpg文件为:',img_names_jpg)

for item_img in img_names_jpg:
    img_names.append(os.path.splitext(item_img)[0])


print(img_names,'\n',len(img_names),'\n')

for item_xml in xml_names_jpg:
    xml_names.append(os.path.splitext(item_xml)[0])

print(xml_names,'\n',len(xml_names))

img_path='/Users/lyl666/Desktop/img_test'
xml_path='/Users/lyl666/Desktop/xml_test'



img_filelist=os.listdir(img_path)
xml_filelist=os.listdir(xml_path)


def rename():

    i=0
    j=0

    file_img_type='.jpg'
    file_xml_type='.xml'
    count=0
    for item_i in img_names:
        for item_x in xml_names:
            if item_i==item_x:
                old_img_file=os.path.join(img_path,img_filelist[i])
                old_xml_file=os.path.join(xml_path,xml_filelist[j])
                new_img_file=os.path.join(img_path,str(int(i+1))+file_img_type)
                new_xml_file=os.path.join(xml_path,str(int(i+1))+file_xml_type)

                os.rename(old_img_file,new_img_file)
                os.rename(old_xml_file,new_xml_file)
                count+=1
            else:
                pass
            j+=1
        i+=1
        j=0
    print("被修改的文件数为："+str(count))
#
#








# for i in len(img_names):
#     for j in len(xml_names):
#         if img_names[i]==xml




#print(os.listdir('/Users/lyl666/Desktop/img_test'))

# print(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir))
# j=0
# for i in os.listdir(os.getcwd()):
#     print(i)
#     j+=1
# print(j)
#
# if(j==len(os.listdir(os.getcwd()))):
#     print("len()函数所求为文件总数量")

# print(os.path.basename(os.getcwd()))
# print(os.name)
# print(os.path.getsize(os.path.abspath(__file__)))
#
# print(__name__)