import json
import models.MtRequest as _mtReq
import core.WebApiSender as _api

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
    "Python sample"  # Text
)

# METHODS ----------------------------------------
def sendGet():
    print("Executing GET request..")

    url = baseUrl+"?gw-username="+mtReq.username+"&gw-password="+mtReq.password+"&gw-from="+mtReq.from_+"&gw-to="+mtReq.to+"&gw-text="+mtReq.text

    resp = api.sendGetRequest(url)    
    print(resp.responseContentString)


def sendPost():
    print("Executing POST request")


def test(data):
    print(data)


# CALLER -----------------------------------------
# TODO: change this between 1 - 2 to switch result
# 1 = Send using POST
# 2 = Send using GET

type = 2
if type == 1:
    sendPost()
elif type == 2:
    sendGet()
