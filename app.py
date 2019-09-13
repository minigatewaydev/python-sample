import json
import models.MtRequest as _mtReq
import core.WebApiSender as _api
import helpers.JsonStringBuilder as _jsonBuilder

baseUrl = "http://162.253.16.28/api/send"
api = _api.WebApiSender

# TODO: change according to your own data
# for username & password. If you set 'dlrMask' to 1,
# please specify the 'dlrUrl'

mtReq = _mtReq.MtRequest(
    "httppostpaid",  # username
    "123456",  # password
    "Python",  # from
    "60123456789",  # to
    "Python sample",  # text
    "0",  # dlrMask
    "",  # dlrUrl
    "1"  # coding
)

jsonBuilder = _jsonBuilder.JsonStringBuilder

# METHODS ----------------------------------------


def sendGet():
    print("Executing GET request..")

    url = baseUrl+"?gw-username="+mtReq.username+"&gw-password="+mtReq.password + \
        "&gw-from="+mtReq.from_+"&gw-to="+mtReq.to+"&gw-text="+mtReq.text

    resp = api.sendGetRequest(url)
    print("Response = " + jsonBuilder.generateJson(resp))


def sendPost():
    print("Executing POST request")
    mtReqJson = jsonBuilder.generateMtReq(mtReq)
    resp = api.sendPostRequest(baseUrl=baseUrl, jsonBody=mtReqJson)
    print("Response = " + jsonBuilder.generateJson(resp))


# CALLER -----------------------------------------
# TODO: change this between 1 - 2 to switch result
# 1 = Send using POST
# 2 = Send using GET

type = 2
if type == 1:
    sendPost()
elif type == 2:
    sendGet()
