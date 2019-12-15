import socketserver,socket

host_ip = "127.0.0.1"
host_port = 50000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host_ip,host_port))
message = input(" -> ")  # take input

while message.lower().strip() != 'bye':
        s.send(message.encode())  # send message
        data = s.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
s.close()  # close the connection
