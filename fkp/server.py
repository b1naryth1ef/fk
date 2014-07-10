from .conn import Connection

class FKServer(Connection):
    def __init__(self, host):
        Connection.__init__(self)
        self.bind(host)

    def handle_hello(self, data):
        print 1337
