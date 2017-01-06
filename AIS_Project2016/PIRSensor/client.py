"""
    This is a client script
"""

from socket import *


class Client(object):
    def __init__(self, host="128.237.165.58", port=15217):
        self.host = host  # host name, type string
        self.port = port  # port name, type integer
        self.sock = socket()  # come on
        self.isReadyToSent = False # ready to change
        self.msg = "Send to sever : client 0 is running"
        # run the function directly
        self.run()
        pass

    # main run function
    def run(self):
        self.sock.connect((self.host, self.port))

        data = self.sock.recv(1024)
        self.client_end(data)

        # self.sock.close()

    # a function running in client end to deal with different things
    def client_end(self, data):
        print "Received from sever : " + data + "\n"

    # a function to send message to the
    def msg_send_to_sever(self, msg):
        print("client: sending to sever")
        self.sock.send(msg)

if __name__ == "__main__":
    client = Client()
