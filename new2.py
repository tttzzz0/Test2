import os
import shutil

images_file_path = './JPEGImages/'
split_data_file_path = './ImageSets/Main/'
new_images_file_path = r'E:\PycharmProjects\detr-main\VOC2COCO\train2017'

if not os.path.exists(new_images_file_path + 'train'):
    os.makedirs(new_images_file_path + 'train')
if not os.path.exists(new_images_file_path + 'val'):
    os.makedirs(new_images_file_path + 'val')
if not os.path.exists(new_images_file_path + 'test'):
    os.makedirs(new_images_file_path + 'test')

dst_train_Image = new_images_file_path + 'train/'
dst_val_Image = new_images_file_path + 'val/'
dst_test_Image = new_images_file_path + 'test/'

total_txt = os.listdir(split_data_file_path)
for i in total_txt:
    name = i[:-4]
    if name == 'train':
        txt_file = open(split_data_file_path + i, 'r')
        for line in txt_file:
            line = line.strip('\n')
            line = line.strip('\r')
            srcImage = images_file_path + line + '.jpg'
            dstImage = dst_train_Image + line + '.jpg'
            shutil.copyfile(srcImage, dstImage)
        txt_file.close()
    elif name == 'val':
        txt_file = open(split_data_file_path + i, 'r')
        for line in txt_file:
            line = line.strip('\n')
            line = line.strip('\r')
            srcImage = images_file_path + line + '.jpg'
            dstImage = dst_val_Image + line + '.jpg'
            shutil.copyfile(srcImage, dstImage)
        txt_file.close()
    elif name == 'test':
        txt_file = open(split_data_file_path + i, 'r')
        for line in txt_file:
            line = line.strip('\n')
            line = line.strip('\r')
            srcImage = images_file_path + line + '.jpg'
            dstImage = dst_test_Image + line + '.jpg'
            shutil.copyfile(srcImage, dstImage)
        txt_file.close()
    else:
        print("Error, Please check the file name of folder")

————————————————
版权声明：本文为CSDN博主「大鹏要高飞」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/a18838956649/article/details/124457462