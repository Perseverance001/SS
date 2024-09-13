import pymssql
import os
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor() #创建游标对象

Bimg_Dir_Paths=['data-HQ/BIMG','data-WQ/BIMG','data-GYM/BIMG','data-SZT/BIMG','data-TXR/BIMG']
Bimg_Dir_ing=Bimg_Dir_Paths[4]
#循环遍历大图文件夹
for filename in os.listdir(Bimg_Dir_ing):
    Bimg_Id=os.path.splitext(filename)[0]
    Bimg_Path=Bimg_Dir_ing+'/'+filename
    Limg_Id=Bimg_Id[:7]
    #写入数据库
    cursor.execute("INSERT INTO BIMG VALUES(%s,%s,%s)",
                   (Bimg_Id,Bimg_Path,Limg_Id))
    conn.commit()
    print(Bimg_Id,Bimg_Path,Limg_Id)