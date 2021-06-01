from utils.MyDB import *
mydb = MyDB()
mydb.connectDB()
sql = 'select * from test_request'
mydb.execute_sql(sql)
result = mydb.get_one(mydb.cursor)
print(result)
