import select
import socket
import queue


server = socket.socket()
server.bind(('localhost', 9000))

server.setblocking(False)

server.listen(1000)

msg_dict = {}
inputs = [server]
outputs = []

while True:

    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    # print(readable, writeable, exceptional)

    for r in readable:
        if r is server:
            conn, addr = server.accept()
            inputs.append(conn)
            msg_dict[conn] = queue.Queue()
        else:
            data = r.recv(1024)
            print('receive: ', data)
            msg_dict[r].put(data)
            outputs.append(r)


    for w in outputs:
        if w in msg_dict:
            if msg_dict[w].qsize() > 0:
                w.send(msg_dict[w].get())
                outputs.remove(w)


    for e in exceptional:
        inputs.remove(e)
        del msg_dict[e]
        if e in outputs:
            outputs.remove(e)