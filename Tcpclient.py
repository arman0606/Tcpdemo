import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',10129))


while True:
    data=input('please input something you want sent to server:')
    if data =='quit':
        break
    s.send(data.encode())

    print(s.recv(1024).decode('utf-8'))
s.send(b'quit')
s.close()
