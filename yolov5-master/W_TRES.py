from datetime import datetime
import pymssql
import train
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor()  # 确认并定位光标位置


UTparameter_Fpath="UTparameter_Fpath"
now = str(datetime.now())
weight_file=train.colorstr('bold', train.opt.save_dir)
print(now[:19])
