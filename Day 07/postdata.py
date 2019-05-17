# -*- coding: utf-8 -*-

import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"Mikkel","language":"German"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_api():
    response = requests.post(Host,data,headers)
    return response

print ( post_api().text )
