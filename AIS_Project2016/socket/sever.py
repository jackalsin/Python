"""
    This is the sever thread
"""
import socket
import sys

HOST = ''  # Symbolic name, all available interfaces
PORT = 15217  # Arbitrary port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a locla host and prot

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error code = ' + str(msg[0]) + "Message = " + msg[1]
    sys.exit(1)
print "Socket binding successful"

# Start listening
s.listen(10)
print 'The server is listening'

# now keep talking with the client

while True:
    # wait to accept a connection
    conn, addr = s.accept()
    print "Connected with " + addr[0] + " : " + str(addr[1])

s.close()