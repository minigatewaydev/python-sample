class SimpleHttpResponse:

    def __init__(self, statusCode, responseContentString, error):
        self.statusCode = statusCode
        self.responseContentString = responseContentString
        self.error = error
