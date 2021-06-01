import pytest
import requests
import json
from utils.ReadRequest import *

readRequest =ReadRequest()

def test_get():
    url = 'https://reqres.in/api/users'
    resp = readRequest.run('get',url,data=None,headers=None)
    print(resp.headers)
    assert resp.status_code == 200


def test_post():
    url = 'https://reqres.in/api/users'
    para ={
            "name": "morpheus",
            "job": "leader"
        }
    headers ={ "Content-type":"application/json" }
    resp = readRequest.run('post',url,data=json.dumps(para),headers=json.dumps(headers))
    print(resp.content)
    print(resp.status_code)
    values = {}
    values = resp.text
    print(values)
    assert resp.status_code == 201

def test_put():
    url = 'https://reqres.in/api/users/2'
    para ={
        "name": "morpheus",
        "job": "zion resident"
        }
    headers ={"Content-type":"application/json" }
    resp = requests.put(url,data=json.dumps(para),headers=headers)
    print(resp.content)
    print(resp.status_code)
    values = {}
    values = resp.text
    print(values)
    assert resp.status_code == 200
