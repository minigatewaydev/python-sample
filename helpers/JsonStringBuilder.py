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
        if hasattr(mtReq, 'dlrMask'):
            jsonData['gw-dlr-mask'] = mtReq.dlrMask
        if hasattr(mtReq, 'dlrUrl'):
            jsonData['gw-dlr-url'] = mtReq.dlrUrl
        jsonData['gw-coding'] = mtReq.coding

        return json.dumps(jsonData)

    def generateJson(obj):
        try:
            return json.dumps(obj.__dict__)
        except Exception as ex:
            return ex
