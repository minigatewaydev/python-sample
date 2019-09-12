import requests as api
import models.SimpleHttpResponse as httpResp
class WebApiSender: 

    def sendGetRequest(baseUrl):
        resp = api.get(baseUrl)
        return httpResp.SimpleHttpResponse(
            resp.status_code,
            resp.text,
            '')
        
