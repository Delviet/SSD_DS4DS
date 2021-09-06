import socket

host = '127.0.0.1'
port = 1234

s = socket.socket()
rq = input("\nEnter your request: ")
s.connect((host, port))
s.send(rq.encode())
s_ans = s.recv(1024)
print(s_ans.decode())
s.close()