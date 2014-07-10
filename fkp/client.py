from .conn import Connection

class FKClient(Connection):
    def __init__(self, host):
        Connection.__init__(self)
        self.connect(host)
