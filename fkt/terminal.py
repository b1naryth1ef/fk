from fkp.client import FKClient
from fkp.api import APIMixin
from fkt.drawing import TextRegion

import thread, sys


class TerminalAPI(APIMixin):
    def api_get_name(self):
        return self.name

class Terminal(TerminalAPI):
    def __init__(self, name, server):
        self.name = name
        self.client = FKClient(server)

        self.interface = None
        self.textr = TextRegion()
        self.line = 0

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
        self.interface.setup(self)
        self.interface.add_region(self.textr)
        self.interface.flip()
        thread.start_new_thread(self.interface.loop, ())

    def handle_key_down(self, key):
        if key == '\r':
            self.line += 1
        self.textr.add_text(self.line, key)

    def handle_key_up(self, key):
        pass

    def handle_quit(self):
        self.call_interface_method("shutdown")
        sys.exit(1)
