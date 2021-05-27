import requests

class Request:
    @classmethod
    def get(cls,values):
        url = values['url']
        response = requests.get(url)
        return response

    @classmethod
    def get(cls, values):
        url = values['url']
        data = values['data']
        headers = values['headers']
        response = requests.get(url,data,headers)
        return response

    @classmethod
    def post(cls, values):
        url = values['url']
        json = values['json']
        headers = values['headers']
        response = requests.get(url, json,headers)
        return response