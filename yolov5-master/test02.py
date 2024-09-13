import os
from pathlib import Path

image_paths = []

# 指定图片文件夹路径
folder_path = 'data/images3'

# 遍历文件夹
for filename in os.listdir(folder_path):

    # 获取图片文件的完整路径
    img_path = os.path.join(folder_path, filename)

    # 判断是否为图片文件
    if Path(img_path).suffix in ['.jpg', '.png', '.jpeg']:  

        # 将图片路径添加到列表
        image_paths.append(img_path)

print(image_paths)
