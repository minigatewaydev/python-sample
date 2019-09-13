import requests as api
import models.SimpleHttpResponse as httpResp

class WebApiSender: 

    def sendGetRequest(url):
        resp = api.get(url)
        return httpResp.SimpleHttpResponse(
            resp.status_code,
            resp.text,
            '')

    def sendPostRequest(baseUrl, jsonBody):
        try:
            resp = api.post(url=baseUrl, json=jsonBody)
            return httpResp.SimpleHttpResponse(
            resp.status_code,
            resp.text,
            ''
            )
        except Exception as ex:
            return httpResp.SimpleHttpResponse(
                '',
                '',
                ex
            )
        
        
        
        
