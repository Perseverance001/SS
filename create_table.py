import pymssql
#数据库连接
conn = pymssql.connect(server='LAPTOP-JO16PU0D', user='sa', password='123456', database='TDARS')
if conn:
    print('数据库连接成功！')
cursor = conn.cursor() #创建游标对象

# 创建LOC表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'LOC') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''
    CREATE TABLE LOC (
        Loc_Id VARCHAR(4) PRIMARY KEY,
        Location VARCHAR(100) NOT NULL,
        Continent VARCHAR(6) NOT NULL,
        Country VARCHAR(20) NOT NULL,
        Detail VARCHAR(100)
    )
''')
    # 提交事务
    conn.commit()

# 创建LIMG表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'LIMG') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE LIMG (
        Limg_Id VARCHAR(7) PRIMARY KEY,
        Limg_Path VARCHAR(50) NOT NULL,
        Loc_Id VARCHAR(4) NOT NULL,
        Shoot_Time VARCHAR(8) NOT NULL,
        FOREIGN KEY (Loc_Id) REFERENCES LOC (Loc_Id)
    )''')
    # 提交事务
    conn.commit()

# 创建BIMG表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'BIMG') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE BIMG (
        Bimg_Id VARCHAR(10) PRIMARY KEY,
        Bimg_Path VARCHAR(50) NOT NULL,
        Limg_Id VARCHAR(7) NOT NULL,
        FOREIGN KEY (Limg_Id) REFERENCES LIMG(Limg_Id)
    )''')
    # 提交事务
    conn.commit()

# 创建SIMG表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'SIMG') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE SIMG (
        Simg_Id VARCHAR(11) PRIMARY KEY,
        Simg_Path VARCHAR(50) NOT NULL,
        Limg_Id VARCHAR(7) NOT NULL,
        Type VARCHAR(10) NOT NULL,
        Ant_Fpath VARCHAR(50) NOT NULL,
        FOREIGN KEY (Limg_Id) REFERENCES LIMG(Limg_Id)
    )''')
    # 提交事务
    conn.commit()

#创建MODEL表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'MODEL') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE MODEL (
        Model_Id INT PRIMARY KEY IDENTITY(1,1),
        Model_name VARCHAR(20) NOT NULL,
        Dparameter_Fpath VARCHAR(50) NOT NULL
    )''')
    # 提交事务
    conn.commit()

#创建USR表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'USR') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE USR (
    Usr_Id INT PRIMARY KEY IDENTITY(10001,1),
    Usr_Name VARCHAR(10) NOT NULL,
    Pswd VARCHAR(20) NOT NULL,
    Email VARCHAR(20) NOT NULL,
    Phone_Num VARCHAR(11) NOT NULL,
    Role VARCHAR(1) NOT NULL DEFAULT '0'
    ) 
    ''')
    # 提交事务
    conn.commit()

#创建TRES表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'TRES') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE TRES (
        Tres_Id INT PRIMARY KEY IDENTITY(1,1),
        Model_Id INT NOT NULL,
        Usr_Id INT NOT NULL,
        UTparameter_Fpath VARCHAR(20) NOT NULL,
        Tres_Time VARCHAR(20) NOT NULL,
        Tres_Fname1 VARCHAR(10) NOT NULL,
        Tres_Fpath1 VARCHAR(50) NOT NULL,
        Tres_Fname2 VARCHAR(10) NOT NULL,
        Tres_Fpath2 VARCHAR(50) NOT NULL,        
        FOREIGN KEY (Model_Id) REFERENCES MODEL(Model_Id),
        FOREIGN KEY (Usr_Id) REFERENCES USR(Usr_Id)
    )''')
    # 提交事务
    conn.commit()

#创建DRES表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'DRES') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE DRES (
        Dres_Id INT PRIMARY KEY IDENTITY(1,1),
        Model_Id INT NOT NULL,
        Usr_Id INT NOT NULL,
        UDparameter_Fpath VARCHAR(20) NOT NULL,
        Dres_Time VARCHAR(20) NOT NULL,
        Dres_Fname1 VARCHAR(10) NOT NULL,
        Dres_Fpath1 VARCHAR(50) NOT NULL,
        Dres_Fname2 VARCHAR(10) NOT NULL,
        Dres_Fpath2 VARCHAR(50) NOT NULL,
        FOREIGN KEY (Model_Id) REFERENCES MODEL(Model_Id),
        FOREIGN KEY (Usr_Id) REFERENCES USR(Usr_Id)
    )''')
    # 提交事务
    conn.commit()

#创建DIMG表
# 判断表是否存在
cursor.execute("SELECT COUNT(*) FROM sys.objects WHERE object_id = OBJECT_ID(N'DIMG') AND type in (N'U')")
table_exists = cursor.fetchone()[0]
if not table_exists:
    cursor.execute('''CREATE TABLE DIMG (
        Dimg_Id INT PRIMARY KEY IDENTITY(1,1),
        Dres_Id INT NOT NULL,
        Bimg_Id VARCHAR(10) NOT NULL,
        Dimg_Path VARCHAR(50) NOT NULL,
        FOREIGN KEY (Dres_Id) REFERENCES DRES(Dres_Id),
        FOREIGN KEY (Bimg_Id) REFERENCES BIMG(Bimg_Id)
    )''')
    # 提交事务
    conn.commit()


# 关闭数据库连接
conn.close()