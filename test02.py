from datetime import datetime
import pymssql
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor()
now = str(datetime.now())[:19]
print(now)
cursor.execute("insert into DRES values(%s,%s,%s,%s,%s,%s,%s,%s)",(1,10001,"",now,'','','',''))

