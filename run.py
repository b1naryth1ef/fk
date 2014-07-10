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

g = GUI()
term.attach_interface(g)

term.show()

text = TextRegion(["YOLO SWAG MUDAFUKA"])
g.add_region(text)

while True:
    time.sleep(1)
