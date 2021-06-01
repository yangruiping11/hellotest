import requests
import json
'''
封装 requests请求中的get与post方法。
'''
class ReadRequest:

    #封装post请求
    def post(self,url,data,headers):
        resp = requests.post(url,json=json.dumps(data),headers=headers)

        return resp

    #封装put请求
    def put(self,url,data,headers):
        '''
        if 'form-data' in headers:
            resp = requests.put(url,data=data,headers=headers)
        elif "Content-type:application/json" in "Content-type:application/json":
        '''
        resp = requests.put(url,json=json.dumps(data),headers=headers)

        return resp

    #封装get请求
    def get(self,url,data,headers):
        if headers !=None:
            resp = requests.get(url,data,headers)
        else:
            resp = requests.get(url,data)

        return resp

    def delete(self,url,data,headers):
        resp = requests.delete(url)
        return resp

    #对封装的请求进行分方法的请求。
    def run(self,method,url,data,headers):
        global resp
        if method == 'get':
            resp = self.get(url,data,headers)
        elif method == 'post':
            resp = self.post(url,data,headers)
        elif method == 'put':
            resp = self.put(url,data,headers)
        elif method == 'delete':
            resp = self.delete(url,data,headers)
        else:
            print("the request method is error")
        return resp

if __name__ == '__main__':
    resp = ReadRequest().run(method='get',url='https://reqres.in/api/users/2',data=None,headers=None)
    print(resp.status_code)
    print(json.dumps(resp.text))
    print(resp.cookies)