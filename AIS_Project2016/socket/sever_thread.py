"""
    This is a file for a thread sever end.
"""

import socket
import sys
from thread import *

HOST = ""  # Symbolic name meaning all available interfaces
PORT = 15217

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"

# Bind socket to host
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print "Bind failed. Error Code = " + str(msg[0]) + " Message = " + msg[1]
    sys.exit(1)
print "Socket binding successfully"

# Start listening on socket
s.listen(10)


# Function for handling connections.
def client_thread(conn):
    # Sending msg to connect
    # Can be used to test
    conn.send("Connected with Sever. Type something and hit enter\n")
    while True:
        # Receive from client
        data = conn.recv(1024)
        reply = "Received. Msg = " + data
        if not data:
            break
        conn.sendall(reply)

    conn.close()

# Code execute

while True:
    # wait to accept a connection
    conn, addr = s.accept()

    print "Connected with " + addr[0] + " : " + str(addr[1])

    # start new thread take 1st argument as a function name to run
    start_new_thread(client_thread, (conn,))

s.close()
