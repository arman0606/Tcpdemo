import socket
import time
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',10129))
s.listen(1)
print('SERVER is running...')
def TCP(sock,addr):
    print('Accept new connection from %s:%s.'%addr)

    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode() =='quit':
            break
        sock.send(data.decode('utf-8').upper().encode('utf-8'))
    sock.close()
    print('connection from %s:%s closed.'%addr)
while True:
    sock,addr =s.accept()
    TCP(sock,addr)
