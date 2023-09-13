"""
A socket sends or receives data in a computer network and contains an IP address and port to which it is sent. Sockets provides communication between
Two computers running on the same network.
Sockets are useful for several reasons:
Sockets allow developers to work directly with the underlying network protocols (TCP/IP or UDP) and provide a common network communication that can be used across different platforms and programming languages.

2. In a client-server configuration, there are two main components:

The server - provides service to customers. It listens for incoming network connections and responds to client requests.
The client- initiates communication with the server to request services or resources.

The sequence of events when there is communication between server and client sockets:
-The server creates a socket and binds it to a specific network address and port and the client creates a socket.
-The server binds its socket to a specific IP address and port, allowing it to listen for incoming connections.
-The server socket goes into listening mode, waiting for incoming connection requests from clients.
-The client socket initiates a connection to the server by specifying the server's IP address and port number.
-When a client connection request is received, the server socket accepts the connection, and creates a new socket dedicated to that client.
- The client and server can send and receive data through their sockets. Data is transferred through read and write operations on the sockets.
-When communication is complete, the client or server can close their sockets to end the connection.

3.
   The constructor of the socket class contains:
    A domain that contains the address family or domain of the socket, which determines whether it will use IPv4 or IPv6 or other communication protocols.
   Socket protocol that specifies the type of socket you want to create, that defines the socket behavior and communication properties.
     Possible options:
       'SOCK_STREAM': for TCP sockets.
       'SOCK_DGRAM': for UDP sockets.

"""