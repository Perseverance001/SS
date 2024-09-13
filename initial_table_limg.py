import pymssql
import os
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor() #创建游标对象

Limg_Dir_Paths=['data-HQ/TIFFImages','data-WQ/TIFFImages','data-GYM/TIFFImages','data-SZT/TIFFimage','data-TXR/TIFFImages']
Limg_Dir_ing=Limg_Dir_Paths[4]
Limg_Id_Shoot_Times=['data-HQ/DataSave/Limg_Id-Shoot_Time.txt','data-WQ/DataSave/Limg_Id-Shoot_Time.txt','data-GYM/BImg-Time.txt','data-SZT/DataSave/Limg_Id-Shoot_Time.txt','data-TXR/Limg time.txt']
LIST_ing=Limg_Id_Shoot_Times[4]
# 循环遍历地点图文件夹
for filename in os.listdir(Limg_Dir_ing):
    # 提取Limg_Id和Loc_Id
    Limg_Id = os.path.splitext(filename)[0]
    Limg_Path = Limg_Dir_ing + '/' + filename
    Loc_Id = Limg_Id[:4]



    # 打开另一个txt文档
    with open(LIST_ing, 'r') as f:
        lines = f.readlines()

    # 查找Loc_Id字符串并提取下一行的Shoot_Time
    for i in range(len(lines)):
        if lines[i].strip() == Limg_Id:
            Shoot_Time = lines[i + 1].strip()
            break
    #写入数据库
    cursor.execute("INSERT INTO LIMG VALUES(%s,%s,%s,%s)",
                   (Limg_Id,Limg_Path,Loc_Id,Shoot_Time))
    conn.commit()
    #打印
    print( Limg_Id,Limg_Path,Loc_Id,Shoot_Time)



