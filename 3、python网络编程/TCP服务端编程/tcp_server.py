"""
author：春夏
python版本：3.9.10 64bit
last_updated：2022.3.22
描述：tcp服务端网络编程
"""

import socket
import threading
import time

new_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

new_server.bind(('127.0.0.1', 9999))

new_server.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新连接:
    sock, addr = new_server.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
