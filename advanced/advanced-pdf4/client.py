import socket

def main():
    message = input("enter message: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345)) 
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"server response: {response}")
    client_socket.close()

if __name__ == "__main__":
    main()
