import os
from PIL import Image
import random

# 获取文件夹下所有文件名
def get_filename(path: str, file_list: list):
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isdir(file_path):
            print("文件夹, 跳过")
            continue
        file_list.append(file_name)
    file_list.sort()


if __name__ == '__main__':
    data_path = 'E:\\707\\flowers\\TW\\datasets\\newimages\\'
    files = list()
    get_filename(data_path, files)
    for i in range(len(files)):
        # 读取图像
        ranum = random.randint(0, 2)
        img_name = data_path + files[i]
        im = Image.open(img_name)

        # 指定逆时针旋转的角度
        if ranum == 0:
            im_rotate = im.transpose(Image.ROTATE_90)
        elif ranum == 1:
            im_rotate = im.transpose(Image.ROTATE_180)
        elif ranum == 2:
            im_rotate = im.transpose(Image.ROTATE_270)

        # 保存图像
        im_rotate.save('E:\\707\\flowers\\TW\\datasets\\newimages\\' + files[i])