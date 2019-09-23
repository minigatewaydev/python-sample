import json
import requests as api
import models.SimpleHttpResponse as httpResp


class RestApiSender:

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

    def sendPostRequest(baseUrl, jsonString):
        try:
            jsonObject = json.loads(jsonString) # the JSON string must be converted into actual JSON object before sending
            resp = api.post(url=baseUrl, json=jsonObject)
            return httpResp.SimpleHttpResponse(
                resp.status_code,
                resp.text, # change to .json() if gw-resp-type is json, otherwise, stay on .text
                ''
            )
        except Exception as ex:
            print(">> API caller exception =")
            print(ex)
