import pymysql
from utils.ReadConfig import *
# 从配置文件中获取指定的参数
host = ReadConfig.get_host()
port = int(ReadConfig.get_port())
user = ReadConfig.get_user()
password = ReadConfig.get_password()
database = ReadConfig.get_database()


#查询所有的数据
def select_table(table_name):
    return format('select * from %s' % table_name)

#打开数据库的连接
db = pymysql.connect(host=host,port=port,user=user,password=password,database=database)
#获取数据库的游标
curso = db.cursor()

# 通过游标执行查询表中所有数据
curso.execute(select_table('test_request'))

#测试所有数据库中获取的数据信息。
# 获取单条数据存储为1个元组。
def get_data():

            data = curso.fetchall()
            for row in data:
                ids = data[0]
                urls = data[1]
                requests_method = data[2]
                jsons = data[3]
                reasons = data[4]
                print(urls)
                print(requests_method)
                print(jsons)
                print(reasons)

            print(data)



#查询指定条件的数据
def select_where_table(table_name, user_name, age):
    return format("select * from %s where name = '%s' and age = %d" % (table_name, user_name, int(age)))


get_data()
