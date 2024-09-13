import pymssql
from PIL import Image
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='Picture')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor()  # 确认并定位光标位置
# 执行SQL查询语句
cursor.execute("SELECT p FROM military_aircraft WHERE id between 1 and 5")
# 获取查询结果
img_paths = cursor.fetchall() #img_paths是一个二维表
print(img_paths)
#遍历图片地址
for img_path in img_paths:
    image=Image.open(img_path[0])#img_path是一个元组，0表示索引第一个元素也就是真正的path
    image.show()# 显示图片
