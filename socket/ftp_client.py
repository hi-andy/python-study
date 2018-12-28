import socket
import hashlib

client = socket.socket()

client.connect(('localhost', 6969))

while True:
    cmd = input('>>>:').strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd.encode('utf8'))
        data_size = client.recv(1024)   # 接收长度
        client.send('received'.encode())    # 解决粘包
        received_size = 0

        print(int(data_size))
        filename = cmd.split()[1]
        f = open(filename + '.new', 'wb')

        m = hashlib.md5()
        total_size = int(data_size) # total will receive data size
        while received_size < total_size:
            remainder_size = total_size - received_size # remainder data size
            receive_size = 1024 if remainder_size > 1024 else remainder_size    # still receive data size
            data = client.recv(receive_size)    # receive the last data size
            f.write(data)
            received_size += len(data)
            m.update(data)

            # print(data_size, received_size)

        else:
            new_md5 = m.hexdigest()
            print('receive done')
            f.close()

        received_md5 = client.recv(1024)    # last receive md5 code , prevent sticky bag.
        print('old md5:', received_md5.decode())
        print('new md5:', new_md5)

client.close()