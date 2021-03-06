import json
import models.MtRequest as _mtReq

class JsonStringBuilder:

    def generateMtReq(mtReq):
        jsonData = {}
        jsonData['gw-username'] = mtReq.username
        jsonData['gw-password'] = mtReq.password
        jsonData['gw-from'] = mtReq.from_
        jsonData['gw-to'] = mtReq.to
        jsonData['gw-text'] = mtReq.text
        jsonData['gw-dlr-mask'] = mtReq.dlrMask
        jsonData['gw-dlr-url'] = mtReq.dlrUrl
        jsonData['gw-coding'] = mtReq.coding
        jsonData['gw-resp-type'] = mtReq.responseType
        return json.dumps(jsonData)

    def generateJson(obj):
        try:
            return json.dumps(obj.__dict__)
        except Exception as ex:
            print(">> JsonStringBuilder exception =")
            print(ex)
