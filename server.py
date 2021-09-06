import socket

counter = 0

s = socket.socket()
ip = '127.0.0.1'
port = 1234

print('Server is up!')
s.bind((ip, port))
s.listen(1)


while True:
    conn, addr = s.accept()
    print(f"Received connection from {addr[0]}:{addr[1]}")

    conn.send(f'Your request is №{counter}'.encode())
    counter += 1
    conn.close()