import socket
from bmupro import b0

# client script
t_port = 5006
tcp_ip = '127.0.0.1'
buf_size = 1024
msg = b0
b.connect((tcp_ip, t_port))
b.send(msg)
data = b.recv(buf_size)
