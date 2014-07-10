#!/usr/bin/env python
from fkp.server import FKServer
from fkt.terminal import Terminal
from fkt.gui import GUI
from fkt.drawing import TextRegion

import thread, time

s = FKServer("ipc:///tmp/fk/1")
thread.start_new_thread(s.parse_loop, ())

term = Terminal("term", "ipc:///tmp/fk/1")
term.connect()
term.attach_interface(GUI)
term.interfaces[0].cache_line_height()
term.show()

reg = TextRegion(term.interfaces[0])
reg.LINES = ["yolo swag nikka"]
reg.draw()

while True:
    time.sleep(1)
