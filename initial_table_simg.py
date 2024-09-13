import pymssql
import os
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor() #创建游标对象

Simg_Dir_Paths=['data-HQ/JPEGImages','data-WQ/JPEGImages','data-GYM/JPEGImages','data-SZT/JPEGImages','data-TXR/JPEGImage'] #切片文件夹
Annotations=['data-HQ/Annotations','data-WQ/Annotations','data-GYM/Annotations','data-SZT/Annotations','data-TXR/Annotations'] #注解文件夹
Simg_Dir_ing=Simg_Dir_Paths[4]
Ant_Fpath_ing=Annotations[4]
#循环遍历大图文件夹
for filename in os.listdir(Simg_Dir_ing):
    Simg_Id=os.path.splitext(filename)[0]
    Simg_Path=Simg_Dir_ing+'/'+filename
    Limg_Id=Simg_Id[:7]
    Ant_Fpath=Ant_Fpath_ing+'/'+Simg_Id+'.xml'
    with open(Ant_Fpath,encoding='UTF-8') as f:
        lines=f.readlines()
        Type=lines[14].strip()[6:-7]
        #写入数据库
        cursor.execute("INSERT INTO SIMG VALUES(%s,%s,%s,%s,%s)",
                       (Simg_Id,Simg_Path,Limg_Id,Type,Ant_Fpath))
        conn.commit()
        print(Simg_Id,Simg_Path,Limg_Id,Type,Ant_Fpath)