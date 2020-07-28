class MtResponse:

    def __init__(self, username, chargingPlan, isSuccess, message, creditDeducted, submitted, mtList):
        self.username = username
        self.chargingPlan = chargingPlan
        self.isSuccess = isSuccess
        self.message = message
        self.creditDeducted = creditDeducted
        self.submitted = submitted
        self.mtList = mtList