import socket
def upper_message(message):
    return message.upper()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  
server_socket.listen(1)
client_socket, client_address = server_socket.accept()
print(f"connection from:{client_address} ")

while True:
    try:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        response = upper_message(data)
        client_socket.send(response.encode('utf-8'))
    except ConnectionResetError:
        print("connection closed by client")
        break
client_socket.close()
server_socket.close()
