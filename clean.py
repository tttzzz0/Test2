# 更改.xml的filename的代码块
import os
import xml.dom.minidom

path='E:\PycharmProjects\detr-main\VOC2007\Annotations_val' # xml文件存放路径
sv_path='E:\PycharmProjects\detr-main\VOC2007\Annotations_val_1' # 修改后的xml文件存放路径
files=os.listdir(path)

for xmlFile in files:
	dom=xml.dom.minidom.parse(os.path.join(path,xmlFile)) #打开xml文件，送到dom解析
	root=dom.documentElement #得到文档元素对象
	item=root.getElementsByTagName('filename') #获取filename这一node名字及相关属性值  # 想更改path 把filename替换成path 同时把下面的i.firstChild.data的输入替换成路径
	a,b=os.path.splitext(xmlFile) #分离出文件名a
	for i in item:
		i.firstChild.data = a + '.jpg'
	with open(os.path.join(sv_path,xmlFile),'w') as fh:
		dom.writexml(fh)
