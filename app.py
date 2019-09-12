import requests as api
import models.SimpleHttpResponse as httpResp
import models.MtRequest as _mtReq
import models.MtResponse as mtResp
import core.WebApiSender as _api

baseUrl = "http://162.253.16.28/api/send"

mtReq = _mtReq.MtRequest(
    "httppostpaid", #username
    "123456", #password
    "Python", #From
    "60123456789", #To
    "Python sample" #Text
    )

api = _api.WebApiSender

def sendGet():
    print("Executing GET request..")
    resp = api.sendGetRequest(baseUrl)

def sendPost():
    print("Executing POST request")

def test(data):
    print(data)

