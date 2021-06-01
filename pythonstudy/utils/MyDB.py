import pymysql
from utils.ReadConfig import *

class MyDB:
    # from config read params
    global host, port, user, password, database
    host = ReadConfig.get_host()
    port = int(ReadConfig.get_port())
    user = ReadConfig.get_user()
    password = ReadConfig.get_password()
    database = ReadConfig.get_database()

    def __init__(self):
        self.db=None
        self.cursor = None

    '''
    open database 
    '''
    def connectDB(self):
        try:
            #connection database
            self.db = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
            #create cursor
            self.cursor = self.db.cursor()
            print("connection database successful")
        except ConnectionError as ex:
            print(ex)

    def execute_sql(self,sql):
         self.connectDB()
         self.cursor.execute(sql)
         self.db.commit()
         return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")