import socket

client = socket.socket()

client.connect(('localhost', 6969))

while True:
    msg = input('>>>:').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf8'))

    data_size = client.recv(1024)   # 接收结果长度
    client.send('received'.encode())    # 解决粘包
    received_size = 0
    received_data = b''
    print(int(data_size))
    while received_size < int(data_size):
        data = client.recv(1024)

        received_size += len(data)
        received_data += data
        print(received_size)

    else:
        print('client receive:', received_data.decode())

client.close()