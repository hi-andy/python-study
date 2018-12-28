import socket

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    msg = input('>>:').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf8'))
    data = client.recv(1024)
    print('client receive:', data.decode())


client.close()