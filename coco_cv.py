import cv2
import random
import json, os
from pycocotools.coco import COCO
from skimage import io
from matplotlib import pyplot as plt

train_json = r'E:\PycharmProjects\detr-main\VOC2COCO\annotations\instances_train2017.json'
train_path = r'E:\PycharmProjects\detr-main\VOC2COCO\train2017'
def visualization_bbox2(num_image, json_path, img_path):
    coco = COCO(json_path)

    list_imgIds = coco.getImgIds(catIds=2)# 获取含有该给定类别的所有图片的id
    img = coco.loadImgs(ids=[list_imgIds[num_image - 1]])[0]  # 获取满足上述要求，并给定显示第num幅image对应的dict
    img_read_path = os.path.join(img_path,img['file_name'])
    image = io.imread(img_read_path)  # 读取图像
    image_name = img['file_name']  # 读取图像名字
    image_id = img['id']  # 读取图像id
    img_annIds = coco.getAnnIds(imgIds=[image_id])
    img_anns = coco.loadAnns(ids=img_annIds)
    for i in range(len(img_annIds)):
        x, y, w, h = img_anns[i - 1]['bbox']  # 读取边框
        image = cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (0, 255, 255), 2)

    plt.rcParams['figure.figsize'] = (20.0, 20.0)
# 此处的20.0是由于我的图片是2000*2000，目前还没去研究怎么利用plt自动分辨率。
    plt.imshow(image)
    plt.show()

if __name__ == "__main__":
   visualization_bbox2(99, train_json, train_path)