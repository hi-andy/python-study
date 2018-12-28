import socket
import os
import time

server = socket.socket()

server.bind(('localhost', 6969)) # 绑定地址&端口

server.listen(5) # 监听

while True:
    conn, addr = server.accept() # 等待接受

    while True:
        data = conn.recv(1024)
        print('server receive:', data.decode())
        if not data:
            print('client has lost ...')
            break
        res = os.popen(data.decode()).read()    # 命令执行结果

        if len(res.encode()) == 0:
            res = 'No results'

        conn.send(str(len(res.encode())).encode())  # 先发送，下面要发送的数据长度
        # time.slee(0.5)
        client_ack = conn.recv(1024) # wait client to confirm 解决粘包
        print('from client ack:', client_ack)
        conn.send(res.encode('utf8'))

server.close()