from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory, connectionDone
from twisted.protocols.basic import LineOnlyReceiver


class Handler(LineOnlyReceiver):
    factory: 'Server'

    def connectionLost(self, reason=connectionDone):
        print("Disconnected")

    def connectionMade(self):
        print("Connected")

    def lineReceived(self, line):
        print(f"Message: {line}")


class Server(ServerFactory):
    protocol = Handler
    clients: list

    def __init__(self):
        self.clients = []

    def startFactory(self):
        print("Server started...")

reactor.listenTCP(
    7410, Server()
)
reactor.run()