# Author: Steven Chen

# Sources used:
# https://realpython.com/python-sockets/#echo-client-and-server
# https://docs.python.org/3/library/socket.html

import socket

# server host and port
host = '127.0.0.1'
port = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect((host, port))

    # print the host and port of the socket we are connected to
    print("Client connected to: {0} \n".format(client_sock.getpeername()))

    while True:
        # get client input and send to server
        client_msg = input(">")
        client_sock.sendall(client_msg.encode())

        # if we send "/q" then we break and close the connection
        if client_msg == "/q":
            break

        # get server response 
        server_response = client_sock.recv(1024).decode()

        # if server sends "/q" then we break and close the connection
        if server_response == "/q":
            break
        
        print("Server: " + server_response)

    print("\nClosing client...")
    client_sock.close()