from fkp.client import FKClient
from fkp.api import APIMixin

import thread, sys


class TerminalAPI(APIMixin):
    def api_get_name(self):
        return self.name

class Terminal(TerminalAPI):
    def __init__(self, name, server):
        self.name = name
        self.client = FKClient(server)

        self.interfaces = []

    def connect(self):
        thread.start_new_thread(self.client.parse_loop, ())
        self.client.send({
            "type": "hello",
            "terminal": {
                "type": "new",
                "name": self.name,
                "session": 0
            }
        })

    def show(self):
        self.call_interface_method("flip")

        for i in self.interfaces:
            thread.start_new_thread(i.loop, ())

    def attach_interface(self, i):
        i.setup(self)
        self.interfaces.append(i)

    def call_interface_method(self, method, args=[], kwargs={}):
        for i in self.interfaces:
            getattr(i, method)(*args, **kwargs)

    def handle_key_down(self, key):
        pass

    def handle_key_up(self, key):
        pass

    def handle_quit(self):
        self.call_interface_method("shutdown")
        sys.exit(1)
