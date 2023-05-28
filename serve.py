import socket

t_port = 60
tcp_ip = '127.0.0.1'
buf_size = 30

b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b.bind((tcp_ip, t_port))
b.listen(1)
con, addr = b.accept()
while True:
    data = con.recv(buf_size)
if not data:
    breakpoint()
print("BMU", data)
con.send(data)
