import zmq, logging

log = logging.getLogger(__name__)

class Connection(object):
    def __init__(self):
        self.log = log

        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.PAIR)

        self.active = True

    def connect(self, host):
        self.sock.connect(host)

    def bind(self, host):
        self.sock.bind(host)

    def send(self, obj):
        self.sock.send_json(obj)

    def parse_loop(self):
        while self.active:
            msg = self.sock.recv_json()

            if hasattr(self, "handle_%s" % msg['type']):
                getattr(self, "handle_%s" % msg['type'])(msg)
                continue

            log.warning("Unhandled message type `%s`", msg['type'])
