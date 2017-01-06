"""
    This is a client script not oop version
    So don't use~
"""

from socket import *

HOST = "localhost"
PORT = 15217

sock = socket()
sock.connect((HOST, PORT))

while True:
    data = sock.recv(1024)
    print data
    sock.send("Client! 1")

sock.close()
