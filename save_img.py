import pymssql
import os        # 这个包是为了后面从文件夹中拿取图片用的
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='Picture')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor()  # 确认并定位光标位置
#创建表
class_target=["entrance","hangars_down","hangars_up","helicopter","helipad","military_aircraft","missile_silos","oil_depot","vehicle"]
for i in range(0,9):
    source_path = rf"D:\Program Files (x86)\data-HQ\HQ-classification\{class_target[i]}" + '\\'  # 图片所在的各文件夹的地址
    cursor.execute(f"""
        if object_id('{class_target[i]}', 'u') is not NULL
        drop table {class_target[i]}
        create table {class_target[i]}(
        id int not NULL,
        p varchar(100),
        primary key(id)
        )
        """)
    conn.commit()  # 写入数据库
    # 从电脑文件夹中获取图片路径并写入数据库
    dirs = os.listdir(source_path)  # 获取文件夹中各个图片
    img_id=0
    for dir in dirs:
        photo_path = os.path.join(source_path, dir)  # 获取各个图片的地址
        cursor.executemany(
            f"insert into {class_target[i]} values(%d,%s)",
            [(img_id+1,photo_path)]
        )
        img_id += 1
    conn.commit()        # 写入数据库
conn.close()
