import pytest
import requests
import json

def test_get():
    url = 'https://reqres.in/api/users'
    resp = requests.get(url)
    print(resp.headers)
    assert  resp.status_code == 200


def  test_post():
    url = 'https://reqres.in/api/users'
    para ={
            "name": "morpheus",
            "job": "leader"
        }
    headers ={ "Content-type":"application/json" }
    resp = requests.post(url,data=json.dumps(para),headers=headers)
    print(resp.content)
    print(resp.status_code)
    values = {}
    values = resp.text
    print(values)
    assert resp.status_code == 201
