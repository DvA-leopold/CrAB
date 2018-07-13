from typing import Tuple, Callable

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer


class Server(TCPServer):
    def __init__(self, address: Tuple[str, int], callback: Callable[[bytes], None]):
        super().__init__()
        self.callback = callback
        Server.listen(self, port=address[1], address=address[0])
        IOLoop.instance().start()
        print('server initialized')

    @gen.coroutine
    def handle_stream(self, stream, address: Tuple[str, int]):
        while True:
            try:
                request = yield stream.read_until_close(callback=self.callback)
                yield stream.write(request)
            except StreamClosedError:
                stream.close(exc_info=True)
                return
