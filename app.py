import urllib.parse as urlparse
import models.MtRequest as _mtReq
import core.WebApiSender as _api
import helpers.JsonStringBuilder as _jsonBuilder

baseUrl = "http://162.253.16.28:5010/api/send"
api = _api.WebApiSender
jsonBuilder = _jsonBuilder.JsonStringBuilder

# TODO: change according to your own data
# for username & password. If you set 'dlrMask' to 1,
# please specify the 'dlrUrl'

mtReq = _mtReq.MtRequest(
    "httppostpaid",  # username
    "123456",  # password
    "Python sample",  # from
    "60123456789",  # to
    "Python sample using HTTP POST & GET",  # text
    "0",  # dlrMask
    "<YOUR-DLR-URL>",  # dlrUrl
    "1",  # coding
    "text"
)

# METHODS ----------------------------------------


def sendGet():
    print("Executing GET request..")

    url = baseUrl+"?gw-username="+mtReq.username+"&gw-password="+mtReq.password + \
        "&gw-from="+urlparse.quote(mtReq.from_) + \
        "&gw-to="+urlparse.quote(mtReq.to)+"&gw-text="+urlparse.quote(mtReq.text) + \
        "&gw-coding="+mtReq.coding+"&gw-dlr-mask="+mtReq.dlrMask+"&gw-dlr-url="+mtReq.dlrUrl + \
        "&gw-resp-type="+mtReq.responseType

    resp = api.sendGetRequest(url)
    print("RESULT = ")
    print(jsonBuilder.generateJson(resp))


def sendPost():
    print("Executing POST request..")
    mtReqJson = jsonBuilder.generateMtReq(mtReq)
    resp = api.sendPostRequest(baseUrl=baseUrl, jsonString=mtReqJson)
    print("RESULT = ")
    print(jsonBuilder.generateJson(resp))


# CALLER -----------------------------------------
# TODO: change 'type' between 1 - 2 to switch result
# 1 = Send using POST
# 2 = Send using GET

type = 1

if type == 1:
    sendPost()
elif type == 2:
    sendGet()
