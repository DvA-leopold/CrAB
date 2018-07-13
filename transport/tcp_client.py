from typing import Tuple, Callable

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient


class Client(TCPClient):
    def __init__(self, address: Tuple[str, int], callback: Callable[[bytes], None]):
        super().__init__()
        self.callback = callback
        self.data = Tuple()
        self.run(address[0], address[1])
        IOLoop.instance().start()
        print('client initialized')

    def send(self, data: str):
        self.data = data

    @gen.coroutine
    def run(self, host: str, port: int):
        stream = yield self.connect(host, port)
        while True:
            if self.data:
                yield stream.write(self.data)
            stream.read_until_close(callback=self.callback)

