# Author: Steven Chen

# Sources used:
# https://realpython.com/python-sockets/#echo-client-and-server
# https://docs.python.org/3/library/socket.html

import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# we use localhost and assign port 9001
host = '127.0.0.1'
port = 9001

# from project instructions to reuse socket
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# binds the socket to the address and port specified above
server_sock.bind((host, port))
# enable the socket to start listening for a client connection
server_sock.listen()

print("Server started - Host: {0} Port: {1}".format(host, port))

# the socket accept method returns a pair (conn, address) 
# "where conn is a new socket object usable to send and receive data on the connection, 
# and address is the address bound to the socket on the other end of the connection."
conn, address = server_sock.accept()

# while the connection is open we run an infinite loop to check for data received
# the with statement is used to automatically close the socket connection
with conn:
    # print the host and process id that is connected to server
    print("Server connected by: {0} \n".format(conn.getpeername()))

    while True:
        client_response = conn.recv(1024).decode()

        # if we get the quit command, then we break the loop
        if client_response == "/q":
            break

        # print message from client
        print("Client: " + str(client_response))

        # get user input to send to the client
        server_msg = input(">")

        # send the message to client
        conn.sendall(server_msg.encode())

        # if we sent a quit command to the client, then server will quit as well
        if server_msg == "/q":
            break

    # when "/q" is received, the loop above is exited and the connection is closed
    print("\nClosing server...")
    conn.close()