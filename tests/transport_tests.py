import unittest

from transport.tcp_client import Client
from transport.tcp_server import Server


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.server = Server(('127.0.0.1', 1984), lambda packet: print(packet))
        self.client = Client(('127.0.0.1', 123457), lambda packet: print(packet))

    def test_simple_echo(self):
        self.client.send('test echo')
        self.server.stop()
