from testexecute.test_pymysql import *
import json
import requests
import pytest
#从数据库中获取单条数据。
#测试执行代码
#获取从数据库中的数据

data = get_data()
print(data)
"""
def test_run():
    if data[1] == "get":
        if data[2] == "None":
            resp = get(data[0])
            print(resp.content)
            assert resp.status_code == int(data[3])
    elif data[1] == "post":
        resp = post(data[0], json.dumps(data[2]))
        print(resp.content)
        assert resp.status_code == int(data[3])
    elif data[1] == "put":
        resp = put(data[0],json.dumps(data[2]))
        print(resp.content)
        assert resp.status_code == int(data[3])


def get(url,param):
    requests.get(url=url,params=param)

def get(url):
    requests.get(url=url)

def post(url,param):
    requests.post(url=url,params=param)

def put(url,param):
    requests.put(url=url,params=param)
"""



if __name__ == '__main__':
    pytest(["-s","test_new_request.py"])

