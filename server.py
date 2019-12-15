import socketserver
import socket

host_ip = "127.0.0.1"
host_port = 50000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host_ip,host_port))
print("Server kuruluyor, baglantı için hazır")
s.listen(5) #5 listener aktif
ip, address = s.accept()  # accept new connection
print("Connection from: " + str(address))
while True:
    # receive data stream. it won't accept data packet greater than 1024 bytes
    data = ip.recv(1024).decode()
    if not data:
        # if data is not received break
        break
    print("from connected user: " + str(data))
    data = input(' -> ')
    ip.send(data.encode())  # send data to the client
ip.close()  # close the connection
