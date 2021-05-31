import pymysql
from utils.ReadConfig import *
import time
# 从配置文件中获取指定的参数
host = ReadConfig.get_host()
port = int(ReadConfig.get_port())
user = ReadConfig.get_user()
password = ReadConfig.get_password()
database = ReadConfig.get_database()


#查询所有的数据
def select_table(table_name):
    return format('select url,requests,jsons,reasons from %s' % table_name)

#打开数据库的连接
db = pymysql.connect(host=host,port=port,user=user,password=password,database=database)
#获取数据库的游标
curso = db.cursor()

# 通过游标执行查询表中所有数据
curso.execute(select_table('test_request'))

#测试所有数据库中获取的数据信息。

def get_data():
    # 获取单条数据存储为1个元组。
    flag = True
    num = 1
    print(str(curso.rowcount) + '行数')
    while flag:
        if num <= curso.rowcount:
            data = curso.fetchone()
            print(data)
        else:
            flag = False
            return data
        num += 1



#查询指定条件的数据
def select_where_table(table_name, user_name, age):
    return format("select * from %s where name = '%s' and age = %d" % (table_name, user_name, int(age)))


get_data()
