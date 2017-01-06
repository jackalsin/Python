"""
    This is a file for a thread sever end.
"""

import socket
import sys
from thread import *


class Sever(object):

    def __init__(self):
        self.host = "128.237.165.58"  # All address are acceptable. type String.
        self.port = 15217 # the port number; type int.

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket created"
        pass

    def execute(self):
        # Bind socket to host
        try:
            self.s.bind((self.host, self.port))
        except socket.error as msg:
            print "Bind failed. Error Code = " + str(msg[0]) + " Message = " + msg[1]
            sys.exit(1)
        print "Socket binding successfully"

        # Start listening on socket
        self.s.listen(10)

        # Code execute

        while True:
            # wait to accept a connection
            conn, addr = self.s.accept()

            print "Connected with " + addr[0] + " : " + str(addr[1])

            # start new thread take 1st argument as a function name to run
            start_new_thread(client_thread, (conn,))

        self.s.close()


# A help function for handling connections.
def client_thread(conn):
    # Sending msg to connect
    # Can be used to test
    conn.send("Connected with Sever. Type something and hit enter\n")
    while True:
        # Receive from client
        data = conn.recv(1024)
        reply = "Received. Msg = " + data
        print "Sever: we receive data from the client " + data
        if not data:
            continue
        conn.sendall(reply)

    conn.close()


if __name__ == "__main__":
    sever = Sever()
    sever.execute()