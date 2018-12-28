import socket
import os
import hashlib

server = socket.socket()

server.bind(('localhost', 6969)) # bind address and port

server.listen(5) # to listen

while True:
    conn, addr = server.accept() # waiting for accept

    while True:
        data = conn.recv(1024)
        print('received cmd:', data.decode())
        if not data:
            print('client has lost ...')
            break
        cmd, filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  # send total data size
            conn.recv(1024) # waiting for act

            for line in f:
                m.update(line)
                conn.send(line)
            f.close()
        conn.send(m.hexdigest().encode())  # last send md5 code
        print('sned done')

server.close()