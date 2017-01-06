from client import Client

client = Client()

while True:
    meg = raw_input("What do you want to send to sever\n")
    client.msg_send_to_sever(meg)
