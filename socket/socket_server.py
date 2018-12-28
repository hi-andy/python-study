import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):


    def handle(self):
        while True:
            try :
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]), self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print(self.client_address, 'client is broken')
                print(e)
                break


if __name__ == '__main__' :
    HOST, PORT = 'localhost', 9999

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)    # only linux

    server.serve_forever()