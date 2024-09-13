import pymssql
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor() #创建游标对象

#各人地点信息表的文件路径
Locations=['data-HQ/Location/location.txt','data-WQ/Location.txt','data-gym/location.txt','data-SZT/Coordinate/Coordinate.txt','data-txr/经纬坐标.txt']
Loc_ing=Locations[4]
# 读取txt文档
with open(Loc_ing, 'r', encoding='UTF-8') as f:
    lines = f.readlines()

# 循环读取数据
for i in range(0, len(lines), 6):
    # 提取数据
    Loc_Id = lines[i].strip()[:4]
    Location = lines[i + 1].strip() + ' ' + lines[i + 2].strip()
    Continent = lines[i + 3].strip()
    Country = lines[i + 4].strip()

    #插入数据到LOC表
    cursor.execute("INSERT INTO LOC VALUES (%s,%s,%s,%s,%s)",
              (Loc_Id, Location, Continent, Country, ''))
    conn.commit()        # 写入数据库

    print(Loc_Id,Location,Continent,Country)