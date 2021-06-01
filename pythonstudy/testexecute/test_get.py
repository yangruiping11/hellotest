from utils.MyDB import *
from utils.ReadRequest import *

myDB = MyDB()
def test_01():
    myDB.connectDB()
    sql = 'select * from test_request limit 1'
    myDB.execute_sql(sql)
    result = myDB.get_one(myDB.cursor)
    request = list(result)
    print(request)
    readRequest = ReadRequest()
    url = request[1]
    method = request[2]
    data = request[3]
    result_code = int(request[4])
    resp = readRequest.run(method,url,data,headers=None)
    assert resp.status_code == result_code

def test_02():
    myDB.connectDB()
    sql = 'select * from test_request limit 1,1'
    myDB.execute_sql(sql)
    result = myDB.get_one(myDB.cursor)
    request = list(result)
    print(request)
    readRequest = ReadRequest()
    url = request[1]
    method = request[2]
    data = request[3]
    result_code = int(request[4])
    #headers = {"Content-type": "application/json"}
    headers =json.load(request[5])
    print(request[5])

    resp = readRequest.run(method, url, data, headers=headers)
    assert resp.status_code == result_code

def test_03():
    s = '12'
    s2 = 'we12'
    assert s in s2
