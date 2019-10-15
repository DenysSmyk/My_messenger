from twisted.internet import reactor
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


class Handler(LineOnlyReceiver):
    def lineReceived(self, line):
        print(line)


class Server(ServerFactory):
    protocol = Handler

    def startFactory(self):
        print("Server started...")

reactor.listenTCP(
    7410, Server()
)
reactor.run()