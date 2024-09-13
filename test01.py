import pymssql
import os
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor()
cursor.execute("select Bimg_Path from BIMG")

# 获取所有查询结果
rows=[]

# 获取所有行数据，并在特定字段前面加上前缀
prefix = '../'
for i in cursor.fetchall():
    rows.append('../'+i[0]);

for row in rows:
    print(row)

# 关闭游标和数据库连接
cursor.close()
conn.close()
