from transport.tcp_client import Client
from transport.tcp_server import Server

server = Server(('127.0.0.1', 1984), lambda packet: print(packet))
client = Client(('127.0.0.1', 1984), lambda packet: print(packet))

