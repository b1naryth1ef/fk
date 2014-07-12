#!/usr/bin/env python
from fkp.server import FKServer
from fkt.terminal import Terminal
from fkt.gui import GUI

import thread, time

s = FKServer("ipc:///tmp/fk/1")
thread.start_new_thread(s.parse_loop, ())

term = Terminal("term", "ipc:///tmp/fk/1")
term.connect()
term.interface = GUI()

term.show()

while True:
    time.sleep(1)
