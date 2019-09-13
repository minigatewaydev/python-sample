import requests as api
import models.SimpleHttpResponse as httpResp

class WebApiSender: 

    def sendGetRequest(url):
        try:
            resp = api.get(url)
            return httpResp.SimpleHttpResponse(
                resp.status_code,
                resp.text,
                ''
                )
        except Exception as ex:
            print(">> API caller exception =")
            print(ex)

    def sendPostRequest(baseUrl, jsonBody):
        try:
            resp = api.post(url=baseUrl)
            return httpResp.SimpleHttpResponse(
            resp.status_code,
            resp.text,
            ''
            )
        except Exception as ex:
            print(">> API caller exception =")
            print(ex)
        
        
        
        
