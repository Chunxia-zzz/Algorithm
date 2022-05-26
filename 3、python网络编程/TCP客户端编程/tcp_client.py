"""
author：春夏
python版本：3.9.10 64bit
last_updated：2022.3.22
描述：tcp客户端网络编程，即模拟浏览器客户端向服务器发送请求
"""

import socket

new_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

new_client.connect(("www.sina.com.cn", 80))

new_client.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = new_client.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

new_client.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

"""
res:

HTTP/1.1 302 Moved Temporarily
Server: nginx
Date: Tue, 22 Mar 2022 09:14:52 GMT
Content-Type: text/html
Content-Length: 138
Connection: close
Location: https://www.sina.com.cn/
X-Via-CDN: f=edge,s=cmcc.xiamen.union.11.nb.sinaedge.com,c=120.237.91.166;
"""
