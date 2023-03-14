import os

saveBasePath = 'E:\PycharmProjects\detr-main\datatxt'  # 存放txt文件的地址
jpgfilepath = r'E:\PycharmProjects\detr-main\a\datasets\VOC2012\Annotations_val'  # jpg图片的地址
ftest = open(os.path.join(saveBasePath, 'val.txt'), 'w')  # 生成的txt文件

temp_jpg = os.listdir(jpgfilepath)  # 获得一个列表
total_jpg = []
print(temp_jpg)
for jpg in temp_jpg:
    if jpg.endswith(".jpg"):
        total_jpg.append(jpg)
num = len(total_jpg)
list = range(num)

for i in list:
    name = total_jpg[i][:-4] + '\n'  # 只取.jpg前面的数字，并且存进name
    ftest.write(name)
ftest.close()


