class MtRequest:

    def __init__(self, username, password, from_, to, text, dlrMask = "0", dlrUrl = "", coding = "1"):
        self.username = username
        self.password = password
        self.from_ = from_
        self.to = to
        self.text = text
        self.dlrMask = dlrMask
        self.dlrUrl = dlrUrl
        self.coding = coding
