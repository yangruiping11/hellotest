import pymysql
from utils.ReadConfig import *
#从配置文件中获取指定的参数
host = ReadConfig.get_host()
port = int(ReadConfig.get_port())
user = ReadConfig.get_user()
password = ReadConfig.get_password()
database = ReadConfig.get_database()

#打开数据库的连接
db = pymysql.connect(host=host,port=port,user=user,password=password,database=database)

curso = db.cursor()

#查询所有的数据
def select_table(table_name):
    return format('select * from %s' % table_name)

#查询指定条件的数据
def select_where_table(table_name, user_name, age):
    return format("select * from %s where name = '%s' and age = %d" % (table_name, user_name, int(age)))


#curso.execute(select_table('testdb'))

curso.execute(select_where_table('testdb','杨瑞','12'))

data = curso.fetchall()

print(data)

curso.close()
db.close()

